<script setup>
import {ref} from "vue";
import fetchCategories from "@/scripts/categories/fetchCategories";
import fetchThreads from "@/scripts/threads/fetchThreads";

const categories = ref(null)
const threads = ref(null)
categories.value = await fetchCategories()
threads.value = (await fetchThreads(null, null, 9)).results
console.log(categories.value)
console.log(threads.value)

</script>

<template>
  <div class="categories">
    <h2 class="cat-heading">Categories</h2>
    <div class="categories-list">
      <div v-for="category in categories" :key="category.id" class="category">
        <router-link :to="{ name: 'category', params: { category: category.slug } }">
          {{ category.name }}
        </router-link>
        <div class="desc">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quisquam, voluptate.
        </div>
      </div>
    </div>
  </div>
  <div class="threads">
    <h2 class="threads-heading">Newest Threads</h2>
    <div class="threads-list">
      <div v-for="thread in threads" :key="thread.id" class="thread">
        <router-link :to="{ name: 'thread', params: { category: thread.category, thread_id: thread.id } }">
          <div class="heading-category">
            <h3 class="thread-heading">{{ thread.subject }}</h3>
            <p class="thread-category">{{
                categories.filter(
                    (cat) => cat.slug === thread.category)[0].name
              }}</p>
          </div>
          <div class="img-text">
            <div class="img">
              <img :src="thread.images[0].image" alt="thread image">
            </div>
            <div class="thread-text">
              <p>{{ thread.text.slice(0, 50) }}...</p>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: #3498db;
  font-size: 20px;
}

a:hover {
  color: #2980b9;
}

.categories-list {
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  justify-content: center;
  align-items: center;
}

.category {
  width: 200px;
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #f6f6f6;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.thread h3 {
  margin-bottom: 10px;
}

.thread p {
  color: #888;
}

h2 {
  text-align: center;
  margin-top: 50px;
}

.cat-heading {
  margin-bottom: 20px;
}

.threads-list {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.thread {
  width: 300px;
  height: 200px;
  padding: 20px;
  border-radius: 10px;
  background-color: #f6f6f6;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.thread-text {
  font-size: 18px;
  display: flex;
  text-align: right;
  align-items: center;
}

.thread-text {
  overflow-wrap: anywhere;
}

.img {
  flex-basis: 100px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}

.img img {
  width: 100%;
}

.img-text {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.heading-category {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.thread-heading {
  font-size: 20px;
}

.threads-heading {
  margin-bottom: 20px;
}
</style>