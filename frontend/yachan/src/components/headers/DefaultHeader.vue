<script setup>
  import { defineProps } from 'vue'

  defineProps(['navItems'])
</script>

<template>
  <div v-for="item in navItems" v-bind:key="item.id">
    <router-link :to="item.url">{{ item.name }}</router-link>
  </div>
</template>

<style scoped>

</style>