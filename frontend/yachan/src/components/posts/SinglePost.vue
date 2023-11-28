<script setup>
import {defineProps, ref} from 'vue'

const props = defineProps(['post'])

const post = ref(props.post);
</script>

<template>
  <div>
    <div class="post-top">
      <div class="subject">
        <p>subject:</p>
        <p>{{ post.subject }}</p>
      </div>
      <div class="author-name" v-if="post.author_name">
        <p>author:</p>
        <p>{{ post.author_name }}</p>
      </div>
      <div class="time-created">
        <p>time created:</p>
        <p>{{ post.time_created.replace('T', ' ').slice(0, -8) }}</p>
      </div>
    </div>
    <div class="images">
      <img v-for="img in post.images" :src="img.image" alt="image" v-bind:key="img.id" class="image">
    </div>
    <div class="text">
      <p>{{ post.text }}</p>
    </div>
  </div>
</template>

<style scoped>

.post-top {
  display: flex;
  gap: 10px;
  font-weight: 700;
}

.image {
  width: 200px;
}
</style>