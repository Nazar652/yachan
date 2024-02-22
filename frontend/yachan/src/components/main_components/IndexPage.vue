<script setup>
import {ref} from "vue";
import fetchCategories from "@/scripts/categories/fetchCategories";
import fetchThreads from "@/scripts/threads/fetchThreads";

const categories = ref(null)
const threads = ref(null)
categories.value = await fetchCategories()
threads.value = await fetchThreads()

</script>

<template>
  <div class="categories">
    <h2>Categories</h2>
    <div class="categories-list">
      <div v-for="category in categories" :key="category.id" class="category">
        <router-link :to="{ name: 'category', params: { category: category.slug } }">
          {{ category.name }}
        </router-link>
      </div>
    </div>
  </div>
  <div class="threads">
    <h2>Newest Threads</h2>
    <div class="threads-list">
      <div v-for="thread in threads" :key="thread.id" class="thread">
        <router-link :to="{ name: 'thread', params: { category: thread.category, thread_id: thread.id } }">
          <h3>{{ thread.subject }}</h3>
          <p>{{ thread.text.slice(0, 100) }}...</p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Navigation Bar */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #3498db;
  color: white;
}

a {
  text-decoration: none;
  color: white;
  font-size: 1.2rem;
}

a:hover {
  color: #f0f0f0;
}

/* New Post Form */
.newPost {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.newPost input, .newPost textarea {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.newPost button {
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #3498db;
  color: white;
  cursor: pointer;
}

.newPost button:hover {
  background-color: #2980b9;
}

/* Thread List */
.thread {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.thread h3 {
  margin-bottom: 10px;
}

.thread p {
  color: #888;
}
</style>