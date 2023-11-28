<script setup>
import {defineProps, ref} from 'vue'

const props = defineProps(['thread'])

const thread = ref(props.thread);
</script>

<template>
  <div>
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
    <div class="post-link">
      <router-link :to="`${thread.category}/${thread.id}`">To thread</router-link>
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
</style>