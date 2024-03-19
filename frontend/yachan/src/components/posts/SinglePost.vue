<script setup>
import {defineProps, ref} from 'vue'
import {getToken} from "@/scripts/global/tokenUtils";
import EditPost from "@/components/posts/EditPost.vue";

const props = defineProps(['post'])
const post = ref(props.post);

let edit = ref(false)
let showOldText = ref(false)

const toggleEdit = () => {
  edit.value = !edit.value;
};

const setEdit = (value) => {
  edit.value = value;
}

const showUpdatedText = () => {
  showOldText.value = false;
}

const showOriginalText = () => {
  showOldText.value = true;
}

</script>

<template>
  <div class="post-container">
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
      <div class="edit" v-if="post.author === getToken() && !post.updated_text" @click="toggleEdit">
        Edit post
      </div>
      <div class="show_old" v-if="post.updated_text" @mouseover="showOriginalText" @mouseleave="showUpdatedText">
        Show old
      </div>
    </div>
    <div class="images">
      <img v-for="img in post.images" :src="img.image" alt="image" v-bind:key="img.id" class="image">
    </div>
    <div class="text">
      <p>{{ post.updated_text ? (showOldText ? post.text : post.updated_text) : post.text }}</p>
    </div>
    <div class="edit-panel" v-if="edit && post.author === getToken() && !post.updated_text">
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

/* styles for post headers: subject, author name, date */
.subject, .author-name, .time-created {
  display: flex;
  gap: 5px;
}

.op {
  background-color: #3498db;
  color: white;
  padding: 5px;
  border-radius: 5px;
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

/* styles for post text */
.text {
  margin-top: 10px;
  font-size: 1.2rem;
}

/* styles for images */

.images {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.images img {
  max-width: 100%;
  max-height: 100%;
}

.post-container {
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 10px;
  max-width: 600px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.post-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
  color: #888;
  margin-bottom: 10px;
}

.text {
  font-size: 1rem;
  line-height: 1.4;
}

.images {
  display: flex;
  gap: 5px;
  overflow-x: auto;
}

.edit, .edit-panel {
  display: none;
}

.post-container:hover .edit, .post-container:hover .edit-panel {
  display: block;
}
</style>