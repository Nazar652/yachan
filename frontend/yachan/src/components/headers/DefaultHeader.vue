<script setup>
  import {defineProps, ref} from 'vue'

  let props = defineProps(['navItems'])
  let navItems = ref(props.navItems)
</script>

<template>
  <header >
      <router-link v-for="item in navItems" v-bind:key="item.id" :to="item.url"><p class="nav-item">{{ item.name }}</p></router-link>
  </header>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=PT+Mono&display=swap');
header {
  display: flex;
  justify-content: center;
  align-items: stretch;
  gap: 5px;
  height: 30px;
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 10px;
  max-width: 600px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: 50px auto;
}

a {
  text-decoration: none;
  color: black;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'PT Mono', monospace;
  text-transform: lowercase;
  flex-basis: 100px;
  background-color: #3498db;
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
}


a:hover {
  background-color: #2980b9;
}
</style>