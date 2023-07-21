<script setup>
  import { ref } from 'vue'
  import axios from 'axios'

  let threads = ref(null)
  axios.get('http://127.0.0.1:8000/api/threads')
  .then(response => {
    threads.value = response.data
  })
  .catch(error => {
    console.error(error)
  })
</script>

<template>
  <div v-for="thread in threads" v-bind:key="thread.id">
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
      <p>{{ thread.time_created }}</p>
    </div>
    <div class="images">
      <img v-for="img in thread.images" :src="img.image" alt="image" v-bind:key="img.id">
    </div>
    <div class="text">
      <p>{{ thread.text }}</p>
    </div>
  </div>
</template>

<style scoped>
</style>