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
      text: text.value,
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

</style>