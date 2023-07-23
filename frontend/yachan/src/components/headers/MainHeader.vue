<script setup>
  import DefaultHeader from "@/components/headers/DefaultHeader.vue";

  const navItems = [
    {
      name: 'Main',
      url: '/'
    },
    {
      name: 'About',
      url: '/about'
    }
  ]
</script>

<template>
  <DefaultHeader :nav-items="navItems" />
</template>

<style scoped>

</style>