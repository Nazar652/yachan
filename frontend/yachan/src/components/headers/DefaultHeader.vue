<script setup>
  import { defineProps } from 'vue'

  const props = defineProps(['navItems'])
  console.log(props.navItems)
</script>

<template>
  <div v-for="item in navItems" v-bind:key="item.id">
    <router-link :to="item.url">{{ item.name }}</router-link>
  </div>
</template>

<style scoped>

</style>