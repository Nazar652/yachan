<script setup>
import {defineProps, onUnmounted, ref, watch} from 'vue'
import NewPost from "@/components/posts/NewPost.vue";
import fetchPosts from "@/scripts/posts/fetchPosts";
import fetchSingleThread from "@/scripts/threads/fetchSingleThread";
import SinglePost from "@/components/posts/SinglePost.vue";
import SingleThread from "@/components/threads/SingleThread.vue";
import {hostname} from "@/scripts/global/globalVariables";
import {useRouter} from 'vue-router';

const router = useRouter();

const props = defineProps(['thread_id'])
const threadId = ref(props.thread_id)
const posts = ref(null)
const thread = ref(null)

const webSocket = new WebSocket(`ws://${hostname}/ws/thread/${threadId.value}/`)
webSocket.onmessage = threadUpdate

async function getThread() {
  thread.value = await fetchSingleThread(threadId.value)
}

async function getPosts() {
  posts.value = await fetchPosts(threadId.value)
}

try {
  await getThread()
  await getPosts()
} catch (e) {
  router.push({name: 'notFound'})
}


watch(() => props.thread_id, async (newThreadId) => {
  threadId.value = newThreadId
  await getThread()
  await getPosts()
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
}
</script>

<template>
  <div v-if="thread !== null">
    <NewPost :thread="thread"></NewPost>

    <SingleThread :thread="thread" :isOpen="true" v-bind:key="thread.text"></SingleThread>

    <div class="posts">
      <div v-for="post in posts" v-bind:key="post.text" class="post">
        <SinglePost :post="post"/>
      </div>
    </div>
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