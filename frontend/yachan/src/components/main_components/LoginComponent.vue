<script setup>

import {ref} from 'vue';
import axios from "axios";

const username = ref('');
const password = ref('');


const submitForm = async () => {
  await axios.get('http://localhost:8000/api/csrf/', {
    withCredentials: true
  })
  const data = {
    username: username.value,
    password: password.value
  }
  await axios.post('http://localhost:8000/api/login/', data, {
    withCredentials: true,
    headers: {
      'X-CSRFToken': document.cookie.split('=')[1],
      'Content-Type': 'application/json'
    }
  })
};
</script>

<template>
  <div class="login-form">
    <h2>Login</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<style scoped>
.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-form h2 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
}

.login-form .form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.login-form .form-group label {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 10px;
}

.login-form .form-group input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.login-form button {
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  background-color: #3498db;
  color: white;
  cursor: pointer;
  width: 100%;
}

form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>