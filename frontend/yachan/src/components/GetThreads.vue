<script setup>

  import { ref } from 'vue'
  import axios from 'axios'
  import {hostname} from "@/scripts/global/globalVariables";

  let threads = ref(null)
  function fetchThreads() {
    axios.get(`${hostname}/api/threads`)
        .then(response => {
          threads.value = response.data
        })
        .catch(error => {
          console.error(error)
        })
  }
  fetchThreads()
  setInterval(fetchThreads, 1000)

</script>

<template>
  <div class="threads">
    <div v-for="thread in threads" v-bind:key="thread.id" class="thread">
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
  </div>
</template>

<style scoped>
  .threads {
    display: flex;
    flex-direction: column;
    max-width: 1200px;
    margin: 50px auto;
    align-items: flex-start;
    gap: 30px;
  }

  .thread {
    padding: 20px;
    border: 1px solid black;
    display: flex;
    flex-direction: column;
    gap: 20px;
    background-color: wheat;
  }

  .thread-top {
    display: flex;
    gap: 10px;
    font-weight: 700;
  }

  .image {
    width: 200px;
  }
</style>