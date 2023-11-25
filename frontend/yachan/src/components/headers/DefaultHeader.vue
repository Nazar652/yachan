<script setup>
  import {defineProps, ref} from 'vue'

  let props = defineProps(['navItems'])
  let navItems = ref(props.navItems)
</script>

<template>
  <header >
      <router-link v-for="item in navItems" v-bind:key="item.id" :to="item.url"><p class="nav-item">/{{ item.name }}/</p></router-link>
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
  transform: skewX(-24deg);
}

.nav-item {

  transform: skewX(24deg);
}

</style>