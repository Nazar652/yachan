<script setup>
  import { ref } from 'vue';
  import useNewThread from '@/components/useNewThread';
  import fetchCategories from "@/components/fetchCategories";

  let categories = ref(null)
  categories.value = await fetchCategories()

  const subject = ref('')
  const text = ref('')
  const author_name = ref('')
  const category = ref('')
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

      await newThread(threadData);

      subject.value = '';
      text.value = '';
      author_name.value = '';
      category.value = '';
      uploaded_images.value.files = null;
    } catch (error) {
      console.error(error);
    }
  }
</script>

<template>
  <p>Categories:</p>
  <p>{{ categories }}</p>
  <form @submit.prevent="submitForm">
    <input v-model="subject" type="text" placeholder="Subject" required />
    <textarea id="text" v-model="text" placeholder="Text" required></textarea>
    <input v-model="author_name" type="text" placeholder="Name" />
    <label for="category">Category:</label>
    <select id="category" v-model="category" required>
      <option v-for="cat in categories" :value="cat.id" v-bind:key="cat.id">{{ cat.name }}</option>
    </select>
    <label for="upload_images">Images:</label>
    <input type="file" id="uploaded_images" ref="uploaded_images" multiple accept="image/*" required>
    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>