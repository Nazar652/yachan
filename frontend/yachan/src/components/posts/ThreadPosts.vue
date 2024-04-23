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

const router = useRouter();

const props = defineProps(['thread_id'])
const threadId = ref(props.thread_id)
const posts = ref(null)
const thread = ref(null)
const pages = ref([])
const page = ref(Number(router.currentRoute.value.query.page) || 1)
const pagesCount = ref(1)


async function getThread() {
  thread.value = await fetchSingleThread(threadId.value)
}


async function getPosts() {
  posts.value = await fetchPosts(threadId.value, page.value)
  pagesCount.value = Math.ceil(posts.value.count / 10)
}

try {
  await getThread()
  await getPosts()
} catch (e) {
  router.push({name: 'notFound'})
}

function makePagesArray() {
  pages.value = []
  for (let i = 1; i <= pagesCount.value; i++) {
    if (i === 1 || i === pagesCount.value || (i >= page.value - 2 && i <= page.value + 2)) {
      pages.value.push(i)
    } else if (pages.value[pages.value.length - 1] !== 0) {
      pages.value.push(0)
    }
  }
}

makePagesArray()

const webSocket = new WebSocket(`ws://${hostname}/ws/thread/${threadId.value}/`)
webSocket.onmessage = threadUpdate

watch(() => props.thread_id, async (newThreadId) => {
  threadId.value = newThreadId
  await getThread()
  await getPosts()
})

watch(() => router.currentRoute.value.query.page, async (newPage) => {
  page.value = Number(newPage)
  await getPosts()
  makePagesArray()
})

onUnmounted(() => {
  webSocket.close()
})

function threadUpdate(event) {
  const newPostData = JSON.parse(event.data);
  if (newPostData.type === "send.posts.update.notification") {
    getPosts()
  } else if (newPostData.type === "send.thread.update.notification") {
    getThread()
    console.log(thread.value)
  }
  makePagesArray()
}
</script>

<template>
  <div v-if="thread !== null">
    <NewPost :thread="thread"></NewPost>

    <SingleThread :thread="thread" :isOpen="true" v-bind:key="thread.text"></SingleThread>

    <div class="posts">
      <div v-for="post in posts.results" v-bind:key="post.text" class="post">
        <SinglePost :post="post"/>
      </div>
    </div>
    <PaginationComponent :link_name="'thread'" :params="{thread_id: threadId}" :page="page"
                         :pages="pages" :pages-count="pagesCount"/>
    <NewPost :thread="thread"></NewPost>
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

</style>