<script setup>
import {defineProps, ref} from 'vue'
import {getToken} from "@/scripts/global/tokenUtils";
import EditPost from "@/components/posts/EditPost.vue";

const props = defineProps(['post'])
const post = ref(props.post);

let edit = ref(false)

const toggleEdit = () => {
  edit.value = !edit.value;
};

const setEdit = (value) => {
  edit.value = value;
}
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
      <div class="op" v-if="post.is_op">OP</div>
      <div class="edit" v-if="post.author === getToken()" @click="toggleEdit">
        Edit post
      </div>
    </div>
    <div class="images">
      <img v-for="img in post.images" :src="img.image" alt="image" v-bind:key="img.id" class="image">
    </div>
    <div class="text">
      <p>{{ post.text }}</p>
    </div>
    <div class="edit-panel" v-if="edit && post.author === getToken()">
      <EditPost :post="post" :setEdit="setEdit"></EditPost>
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