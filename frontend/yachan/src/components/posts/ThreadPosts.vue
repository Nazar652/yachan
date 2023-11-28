<script setup>
import {defineProps, onUnmounted, ref, watch} from 'vue'
import NewPost from "@/components/posts/NewPost.vue";
import fetchPosts from "@/scripts/posts/fetchPosts";
import fetchSingleThread from "@/scripts/threads/fetchSingleThread";
import SinglePost from "@/components/posts/SinglePost.vue";

const props = defineProps(['thread_id'])
const threadId = ref(props.thread_id)
const posts = ref(null)
const thread = ref(null)

thread.value = await fetchSingleThread(threadId.value)
async function getPosts() {
  posts.value = await fetchPosts(threadId.value)
}

getPosts()
const intervalId = setInterval(getPosts, 1000)
watch(() => props.thread_id, (newThread) => {
  threadId.value = newThread
})

onUnmounted(() => {
  clearInterval(intervalId)
})
</script>

<template>
  <NewPost :threadId="$route.params.thread_id"></NewPost>

  <div class="thread">
    <div class="thread-top">
      <div class="subject">
        <p>subject:</p>
        <p>{{ thread.subject }}</p>
      </div>
      <div class="author-name" v-if="thread.author_name">
        <p>author:</p>
        <p>{{ thread.author_name }}</p>
      </div>
      <div class="time-created">
        <p>time created:</p>
        <p>{{ thread.time_created.replace('T', ' ').slice(0, -8) }}</p>
      </div>
    </div>
    <div class="images">
      <img v-for="img in thread.images" :src="img.image" alt="image" v-bind:key="img.id" class="image">
    </div>
    <div class="text">
      <p>{{ thread.text }}</p>
    </div>
  </div>

  <div class="posts">
    <div v-for="post in posts" v-bind:key="post.id" class="post">
      <SinglePost :post="post"/>
    </div>
  </div>

  <NewPost :threadId="$route.params.thread_id"></NewPost>
</template>

<style scoped>

  .thread-top {
    display: flex;
    gap: 10px;
    font-weight: 700;
  }

  .image {
    width: 200px;
  }

  .thread, .post {
    padding: 20px;
    border: 1px solid black;
    display: flex;
    flex-direction: column;
    gap: 20px;
    background-color: wheat;
  }

  .posts {
    display: flex;
    flex-direction: column;
    max-width: 1200px;
    margin: 50px auto;
    align-items: flex-start;
    gap: 30px;
  }
</style>