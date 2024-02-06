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
  gap: 10px;
  font-weight: 700;
}

.image {
  width: 200px;
}

.thread {
  padding: 20px;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  gap: 20px;
  background-color: wheat;
}
</style>