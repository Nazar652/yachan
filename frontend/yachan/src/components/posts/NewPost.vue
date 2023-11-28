<script setup>
import { ref, defineProps } from 'vue';
  import createNewPost from '@/scripts/posts/createNewPost'

  const props = defineProps(['threadId'])

  const subject = ref('')
  const text = ref('')
  const author_name = ref('')
  const threadId = ref(props.threadId)
  const uploaded_images = ref(null)

  const { newPost } = createNewPost()

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
        thread: threadId.value,
        uploaded_images: uploaded_images.value.files,
        author: 'author'
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
      <div>
        <input v-model="subject" type="text" placeholder="Subject" />
        <input v-model="author_name" type="text" placeholder="Name" />
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
    margin: 50px;
  }
  form {
    display: flex;
    flex-direction: column;
  }
</style>