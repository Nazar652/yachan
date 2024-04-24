<script setup>
import {defineProps, ref, watchEffect} from 'vue'
import {getToken} from "@/scripts/global/tokenUtils";
import EditPost from "@/components/posts/EditPost.vue";

const props = defineProps(['post', 'inThread'])
const post = ref(props.post);
const inThread = ref(props.inThread)

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

watchEffect(() => {
  post.value = props.post
})

</script>

<template>
  <div class="post-container">
    <div class="post-top">
      <div class="post-id">
        <p>ID: {{ post.id }}</p>
      </div>
      <div class="subject" v-if="post.subject">
        <p>{{ post.subject }}</p>
      </div>
      <div class="author-name">
        <p class="author-name-text"><span v-if="post.author_name">{{ post.author_name }}</span> <span
            class="you-mark" v-if="post.author === getToken()">(You)</span></p>
      </div>
      <div class="op" v-if="post.is_op">OP</div>
      <div class="edit" v-if="post.author === getToken() && !post.updated_text" @click="toggleEdit">
        Edit post
      </div>
      <div class="show_old" v-if="post.updated_text" @mouseover="showOriginalText" @mouseleave="showUpdatedText">
        Show old
      </div>
    </div>
    <div class="img-text">
      <div class="images" :class="{smallImages:!inThread}" v-if="post.images.length">
        <div class="image-block" v-for="img in post.images" v-bind:key="img.id">
          <img :src="img.image" alt="image" class="image"
               :class="{smallImage:!inThread}">
        </div>
      </div>
      <div class="text-time">
        <div class="text">
          <p v-if="inThread">{{ post.updated_text ? (showOldText ? post.text : post.updated_text) : post.text }}</p>
          <p v-else>{{
              post.updated_text ? (showOldText ? post.text.slice(0, 300) : post.updated_text.slice(0, 300)) : post.text.slice(0, 300)
            }}...</p>
        </div>
        <div class="edit-panel" v-if="edit && post.author === getToken() && !post.updated_text">
          <EditPost :post="post" :setEdit="setEdit"></EditPost>
        </div>
        <div class="time-created">
          <p>{{ post.time_created.replace('T', ' ').slice(0, -8) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>


.image {
  width: 200px;
}

.smallImage {
  width: 100px;
}

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
  border-radius: 5px;
  cursor: pointer;
  height: 30px;
  width: 80px;
}

.edit-panel {
  margin-top: 10px;
  align-self: flex-start;
  width: 100%;
}

/* styles for post text */
.text {
  margin-top: 10px;
  font-size: 1.2rem;
  overflow-wrap: anywhere;
}

/* styles for images */

.images {
  display: grid;
  margin-top: 10px;
  grid-template-columns: repeat(auto-fit, 200px);
  grid-gap: 10px;
  max-width: 620px;
}

.smallImages {
  grid-template-columns: repeat(auto-fit, 100px);
  max-width: 320px;
  max-height: 210px;
}

.post-container {
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.post-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  height: 20px;
}

.post-top, .time-created {
  font-weight: 700;
  font-size: 14px;
  color: #888;
}

.text {
  font-size: 1rem;
  line-height: 1.4;
}

.edit, .edit-panel {
  display: none;
}

.post-container:hover .edit, .post-container:hover .edit-panel {
  display: block;
}

.post-container:hover .edit {
  display: flex;
  align-items: center;
  justify-content: center;
}

.img-text {
  display: flex;
  gap: 20px;
}

.text-time {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
  flex-grow: 1;
}

.text {
  align-self: flex-start;
}
</style>