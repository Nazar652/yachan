<script setup>
import {defineProps, ref} from 'vue'
import {getToken} from "@/scripts/global/tokenUtils";
import EditThread from "@/components/threads/EditThread.vue";

const props = defineProps(['thread', 'isOpen'])
const thread = ref(props.thread)
const isOpen = ref(props.isOpen)

let edit = ref(false)

const toggleEdit = () => {
  edit.value = !edit.value;
};

const setEdit = (value) => {
  edit.value = value;
};

</script>

<template>
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
      <div class="edit" v-if="thread.author === getToken()" @click="toggleEdit">
        Edit thread
      </div>
    </div>
    <div class="images">
      <img v-for="img in thread.images" :src="img.image" alt="image" v-bind:key="img.id" class="image">
    </div>
    <div class="text">
      <p>{{ thread.text }}</p>
    </div>
    <div class="edit-panel" v-if="edit && thread.author === getToken()">
      <EditThread :thread="thread" :setEdit="setEdit"></EditThread>
    </div>
    <div class="post-link" v-if="!isOpen">
      <router-link :to="{ name: 'thread', params: { category: thread.category, thread_id: thread.id }}">To thread</router-link>
    </div>
  </div>
</template>

<style scoped>
.thread-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
  color: #888;
  margin-bottom: 10px;
}

.image {
  width: 200px;
}

.subject, .author-name, .time-created {
  display: flex;
  gap: 5px;
}

.edit {
  background-color: #3498db;
  color: white;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
}

.edit-panel {
  margin-top: 10px;
}

.text {
  margin-top: 10px;
  font-size: 1.2rem;
}

.images {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.images img {
  max-width: 100%;
  max-height: 100%;
}

.thread {
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 10px;
  max-width: 600px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.thread:hover .edit, .thread:hover .edit-panel {
  display: block;
}
</style>