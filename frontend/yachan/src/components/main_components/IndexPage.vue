<script setup>
import {ref} from "vue";
import fetchCategories from "@/scripts/categories/fetchCategories";

const categories = ref(null)
categories.value = await fetchCategories()

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
</template>

<style scoped>
.categories-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
.category {
  margin: 0.5rem 0;
}
.categories a {
  text-decoration: none;
  color: black;
  font-weight: bold;
  font-size: 1.2rem;
}
.categories a:hover {
  color: blue;
}
.categories h2 {
  margin: 1rem 0;
}
</style>