<script setup>
import {defineProps, ref, onUnmounted, watchEffect} from 'vue'
import {getToken} from "@/scripts/global/tokenUtils";
import EditThread from "@/components/threads/EditThread.vue";
import fetchPosts from "@/scripts/posts/fetchPosts";
import {hostname} from "@/scripts/global/globalVariables";
import {useRouter} from 'vue-router';
import SinglePost from "@/components/posts/SinglePost.vue";

const router = useRouter();

const props = defineProps(['thread', 'isOpen', 'posts'])
const thread = ref(props.thread)
const isOpen = ref(props.isOpen)
const edit = ref(false)
const posts = ref(props.posts)
let showOldText = ref(false)


const toggleEdit = () => {
  edit.value = !edit.value;
};

const setEdit = (value) => {
  edit.value = value;
};

async function getPosts() {
  posts.value = await fetchPosts(thread.value.id)
}

const showUpdatedText = () => {
  showOldText.value = false;
}

const showOriginalText = () => {
  showOldText.value = true;
}

try {
  await getPosts()
} catch (e) {
  router.push({name: 'notFound'})
}

const webSocket = new WebSocket(`ws://${hostname}/ws/thread/${thread.value.id}/`)
webSocket.onmessage = threadUpdate

onUnmounted(() => {
  webSocket.close()
})

watchEffect(() => {
  thread.value = props.thread
})

function threadUpdate(event) {
  const newPostData = JSON.parse(event.data);
  if (newPostData.type === "send.posts.update.notification") {
    getPosts()
  }
}
</script>

<template>
  <div class="thread">
    <div class="thread-main">
      <div>
        <div class="thread-top">
          <div class="thread-id">
            <p>ID: {{ thread.id }}</p>
          </div>
          <div class="subject">
            <p class="subject-text">{{ thread.subject }}</p>
          </div>
          <div class="author-name">
            <p class="author-name-text"><span v-if="thread.author_name">{{ thread.author_name }}</span> <span
                class="you-mark" v-if="thread.author === getToken()">(You)</span></p>
          </div>
          <div class="edit" v-if="thread.author === getToken()" @click="toggleEdit">
            Edit thread
          </div>
          <div class="show_old" v-if="thread.updated_text" @mouseover="showOriginalText" @mouseleave="showUpdatedText">
            Show old
          </div>
        </div>
        <div class="images">
          <img v-for="img in thread.images" :src="img.image" alt="image" v-bind:key="img.id" class="image">
        </div>
        <div class="text">
          <p>{{ thread.updated_text ? (showOldText ? thread.text : thread.updated_text) : thread.text }}</p>
        </div>
        <div class="edit-panel" v-if="edit && thread.author === getToken() && !thread.updated_text">
          <EditThread :thread="thread" :setEdit="setEdit"></EditThread>
        </div>
      </div>
      <div class="bottom-thread">
        <div class="post-link" v-if="!isOpen">
          <router-link :to="{ name: 'thread', params: { category: thread.category, thread_id: thread.id }}">To thread
          </router-link>
        </div>
        <div class="time-created">
          <p>{{ thread.time_created.replace('T', ' ').slice(0, -8) }}</p>
        </div>
      </div>
    </div>
    <div class="thread-posts" v-if="!isOpen">
      <div class="latest-posts">
        Latest posts:
      </div>
      <div class="posts">
        <div v-for="post in posts.results.slice(0, 4)" v-bind:key="post.text" class="post">
          <SinglePost :post="post" :in-thread="false"/>
        </div>
        <div class="nobody-post" v-if="!posts.results.length">Nobody posted anything yet</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.thread-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.thread-top > *, .latest-posts, .time-created, .nobody-post {
  font-size: 18px;
  color: #888;
  margin-bottom: 10px;
}

.image {
  width: 200px;
}

.edit, .post-link a {
  background-color: #3498db;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.post-link a {
  text-decoration: none;
}

.edit-panel {
  margin-top: 10px;
  width: 100%;
}

.text {
  margin-top: 10px;
  font-size: 1.2rem;
}

.images {
  display: flex;
  gap: 10px;
  margin-top: 10px;
  flex-wrap: wrap;
  justify-content: flex-start;
}


.thread {
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 10px 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  display: flex;
  gap: 20px;
}

.thread-main {
  flex-grow: 1;
  flex-basis: 50%;
  display: flex;
  flex-direction: column;
  gap: 15px;
  justify-content: space-between;
}

.thread-posts {
  flex-grow: 1;
  flex-basis: 50%;
}

.thread:hover .edit, .thread:hover .edit-panel {
  display: block;
}

.bottom-thread {
  display: flex;
  justify-content: space-between;
}

.you-mark {
  font-weight: 700;
}
</style>