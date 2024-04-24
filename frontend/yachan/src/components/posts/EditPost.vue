<script setup>
import {defineProps, ref} from "vue";
import updatePost from "@/scripts/posts/updatePost";

const props = defineProps(['post', 'setEdit'])

const post = ref(props.post)
const text = ref(post.value.text)

const {editPost} = updatePost()

const submitForm = async () => {
  try {
    const newData = {
      id: post.value.id,
      updated_text: text.value,
    };
    await editPost(newData);
    props.setEdit(false)
  } catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <form @submit.prevent="submitForm" id="editPostForm">
    <textarea id="text" v-model="text" placeholder="New Text" required></textarea>
    <button type="submit">Edit</button>
  </form>
</template>

<style scoped>
#editPostForm {
  display: flex;
  flex-direction: column;
}

#editPostForm textarea {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #888;
}

#editPostForm button {
  background-color: #3498db;
  color: white;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
  border: none;
  width: 50px;
  align-self: flex-end;
}

#editPostForm button:hover {
  background-color: #2980b9;
}
</style>