<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";
import isAuthenticated from "@/scripts/global/isAuthenticated";

const authenticated = ref(false);

onMounted(async () => {
  authenticated.value = await isAuthenticated();
});


const logout = async () => {
  await axios.get('http://localhost:8000/api/csrf/', {
    withCredentials: true
  })
  await axios.post('http://localhost:8000/api/logout/', {}, {
    withCredentials: true,
    headers: {
      'X-CSRFToken': document.cookie.split('=')[1],
      'Content-Type': 'application/json'
    }
  })
};
</script>

<template>
  <div v-if="authenticated">
    <button @click="logout">Logout</button>
  </div>
</template>

<style scoped>

</style>