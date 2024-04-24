<script setup>
import {ref, defineProps, watch} from 'vue';
import createNewThread from '@/scripts/threads/createNewThread'
import {getToken} from "@/scripts/global/tokenUtils";

const props = defineProps(['category'])

const subject = ref('')
const text = ref('')
const author_name = ref('')
const category = ref(props.category)
const uploaded_images = ref(null)

const {newThread} = createNewThread()

const submitForm = async () => {
  try {
    if (uploaded_images.value.files.length > 5) {
      alert("You can only upload a maximum of 5 images")
      return
    }
    const threadData = {
      subject: subject.value,
      text: text.value,
      author_name: author_name.value,
      category: category.value,
      uploaded_images: uploaded_images.value.files,
      author: getToken()
    };
    await newThread(threadData);

    subject.value = '';
    text.value = '';
    author_name.value = '';
    uploaded_images.value.value = null;
  } catch (error) {
    console.error(error);
  }
}
watch(() => props.category, (newSlug) => {
  category.value = newSlug
});
</script>

<template>
  <div class="newThread">
    <form @submit.prevent="submitForm" id="newThreadForm">
      <h2>New Thread</h2>
      <div>
        <input v-model="subject" type="text" placeholder="Subject" required/>
        <input v-model="author_name" type="text" placeholder="Name"/>
      </div>
      <textarea id="text" v-model="text" placeholder="Text" required></textarea>
      <label for="upload_images">Images:</label>
      <input type="file" id="uploaded_images" ref="uploaded_images" multiple accept="image/*" required>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.newThread {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 10px;
  max-width: 600px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.newThread form {
  display: flex;
  flex-direction: column;
}

.newThread input, .newThread textarea {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #888;
}

.newThread button {
  background-color: #3498db;
  color: white;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
  border: none;
}

.newThread button:hover {
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