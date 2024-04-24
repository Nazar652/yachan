<script setup>
import {defineProps, ref} from "vue";
import updateThread from "@/scripts/threads/updateThread";

const props = defineProps(['thread', 'setEdit'])

const thread = ref(props.thread)
const text = ref(thread.value.text)

const {editThread} = updateThread()

const submitForm = async () => {
  try {
    const newData = {
      id: thread.value.id,
      updated_text: text.value,
    };
    await editThread(newData);
    props.setEdit(false)
  } catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <form @submit.prevent="submitForm" id="editThreadForm">
    <textarea id="text" v-model="text" placeholder="New Text" required></textarea>
    <button type="submit">Edit</button>
  </form>
</template>

<style scoped>
#editThreadForm {
  display: flex;
  flex-direction: column;
}

#editThreadForm textarea {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #888;
}

#editThreadForm button {
  background-color: #3498db;
  color: white;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
  border: none;
  width: 50px;
  align-self: flex-end;
}

#editThreadForm button:hover {
  background-color: #2980b9;
}
</style>