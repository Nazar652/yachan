<script setup>
  import fetchCategories from "@/scripts/fetchCategories";
  import DefaultHeader from "@/components/headers/DefaultHeader.vue";

  const categories = await fetchCategories()
  const navItems = [
      {
      name: 'Main',
      url: '/'
    }
  ]
  for (const cat of categories) {
    navItems.push(
        {
          name: cat.name,
          url: '/' + cat.slug
        }
    )
  }
</script>

<template>
  <DefaultHeader :nav-items="navItems" />
</template>

<style scoped>

</style>