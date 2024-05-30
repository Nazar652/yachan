<script setup>
import {ref, defineProps} from 'vue';
import createNewPost from '@/scripts/posts/createNewPost'
import {getToken} from "@/scripts/global/tokenUtils";

const props = defineProps(['thread'])

const subject = ref('')
const text = ref('')
const author_name = ref('')
const thread = ref(props.thread)
const uploaded_images = ref(null)

const {newPost} = createNewPost()

const submitForm = async () => {
  try {
    if (uploaded_images.value.files.length > 5) {
      alert("You can only upload a maximum of 5 images")
      return
    }
    let is_op = false
    if (thread.value.author === getToken()) {
      is_op = true
    }
    const threadData = {
      subject: subject.value,
      text: text.value,
      author_name: author_name.value,
      thread: thread.value.id,
      uploaded_images: uploaded_images.value.files,
      author: getToken(),
      is_op: is_op
    };
    await newPost(threadData);

    subject.value = '';
    text.value = '';
    author_name.value = '';
    uploaded_images.value.value = null;

  } catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <div class="newPost">
    <form @submit.prevent="submitForm">
      <h2>New Post</h2>
      <div>
        <input v-model="subject" type="text" placeholder="Subject"/>
        <input v-model="author_name" type="text" placeholder="Name"/>
      </div>
      <textarea id="text" v-model="text" placeholder="Text" required></textarea>
      <label for="upload_images">Images:</label>
      <input type="file" id="uploaded_images" ref="uploaded_images" multiple accept="image/*">
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.newPost {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 10px;
  max-width: 600px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.newPost form {
  display: flex;
  flex-direction: column;
}

.newPost input, .newPost textarea {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #888;
}

.newPost button {
  background-color: #3498db;
  color: white;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
  border: none;
}

.newPost button:hover {
  background-color: #2980b9;
}

h2 {
  text-align: center;
  margin-bottom: 10px;
  color: #888;
  font-size: 24px;
  font-weight: 700;
}
</style>