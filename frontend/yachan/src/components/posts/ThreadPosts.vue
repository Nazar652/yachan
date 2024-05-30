<script setup>
import {defineProps, onUnmounted, ref, watch} from 'vue'
import NewPost from "@/components/posts/NewPost.vue";
import fetchPosts from "@/scripts/posts/fetchPosts";
import fetchSingleThread from "@/scripts/threads/fetchSingleThread";
import SinglePost from "@/components/posts/SinglePost.vue";
import SingleThread from "@/components/threads/SingleThread.vue";
import {hostname} from "@/scripts/global/globalVariables";
import {useRouter} from 'vue-router';
import PaginationComponent from "@/components/main_components/PaginationComponent.vue";
import isAuthenticated from "@/scripts/global/isAuthenticated";

const router = useRouter();

const props = defineProps(['thread_id'])
const threadId = ref(props.thread_id)
const posts = ref(null)
const thread = ref(null)
const page = ref(Number(router.currentRoute.value.query.page) || 1)
const authenticated = ref(false)


async function getThread() {
  thread.value = await fetchSingleThread(threadId.value)
}


async function getPosts() {
  const newPosts = await fetchPosts(threadId.value, page.value)
  posts.value = []
  posts.value = await newPosts
}

try {
  await getThread()
  await getPosts()
} catch (e) {
  router.push({name: 'notFound'})
}

const webSocket = new WebSocket(`ws://${hostname}/ws/thread/${threadId.value}/`)
webSocket.onmessage = threadUpdate

watch(() => props.thread_id, async (newThreadId) => {
  threadId.value = newThreadId
  await getThread()
  await getPosts()
  page.value = 1
})

watch(() => router.currentRoute.value.query.page, async (newPage) => {
  page.value = Number(newPage)
  await getPosts()
})

authenticated.value = await isAuthenticated()


onUnmounted(() => {
  webSocket.close()
})

function threadUpdate(event) {
  const newPostData = JSON.parse(event.data);
  if (newPostData.type === "send.posts.update.notification") {
    getPosts()
  } else if (newPostData.type === "send.thread.update.notification") {
    getThread()
  }
}
</script>

<template>
  <div v-if="thread !== null">
    <div class="thread-new-post">
      <SingleThread :thread="thread" :isOpen="true" v-bind:key="thread.text" :authenticated="authenticated"></SingleThread>
      <NewPost :thread="thread"></NewPost>
    </div>
    <PaginationComponent :link_name="'thread'" :params="{thread_id: threadId}" :count="posts.count"
                         :page="page" :delim="10"/>
    <div class="posts">
      <div v-for="post in posts.results" v-bind:key="post.text" class="post">
        <SinglePost :post="post" :in-thread="true" :authenticated="authenticated"/>
      </div>
    </div>
  </div>
</template>

<style scoped>

.posts {
  display: flex;
  flex-direction: column;
  max-width: 1200px;
  margin: 50px auto;
  align-items: flex-start;
  gap: 30px;
}

.thread-new-post {
  display: flex;
  gap: 30px;
  margin-bottom: 40px;
}

.thread-new-post > *{
  flex-basis: 50%;
}

</style>