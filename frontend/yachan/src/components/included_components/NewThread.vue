<script setup>
  import { ref, defineProps } from 'vue';
  import useNewThread from '@/scripts/useNewThread'
  import {hostname} from "@/scripts/globalVariables"

  const props = defineProps(['category'])

  const subject = ref('')
  const text = ref('')
  const author_name = ref('')
  const category = ref(props.category)
  const uploaded_images = ref(null)

  const { newThread } = useNewThread()

  const submitForm = async () => {
    try {
      const threadData = {
        subject: subject.value,
        text: text.value,
        author_name: author_name.value,
        category: category.value,
        uploaded_images: uploaded_images.value.files,
        author: 'author'
      };
      console.log(threadData)
      await newThread(threadData, `${hostname}/api/threads/`);

      subject.value = '';
      text.value = '';
      author_name.value = '';
      uploaded_images.value.files = null;
    } catch (error) {
      console.error(error);
    }
  }
</script>

<template>
  <div class="newThread">
    <form @submit.prevent="submitForm">
      <div>
        <input v-model="subject" type="text" placeholder="Subject" required />
        <input v-model="author_name" type="text" placeholder="Name" />
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
    margin: 50px;
  }
  form {
    display: flex;
    flex-direction: column;
  }
</style>