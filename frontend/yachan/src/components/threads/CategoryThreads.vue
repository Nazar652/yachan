<script setup>
import NewThread from "@/components/threads/NewThread.vue";
import fetchThreads from "@/scripts/threads/fetchThreads";
import {defineProps, onUnmounted, ref, watch} from "vue";
import SingleThread from "@/components/threads/SingleThread.vue";
import {hostname} from "@/scripts/global/globalVariables";



const props = defineProps(['category'])
const category = ref(props.category)
const threads = ref(null)

const webSocket = new WebSocket(`ws://${hostname}/ws/category/${category.value}/`)
webSocket.onmessage = categoryUpdate

async function getThreads() {
  threads.value = await fetchThreads(category.value)
  console.log(threads.value)
}

await getThreads()


watch(() => props.category, (newSlug) => {
  category.value = newSlug
  getThreads()
});

onUnmounted(() => {
  webSocket.close()
})

function categoryUpdate(event) {
  console.log(event.data)
  getThreads()
}
</script>

<template>
  <NewThread :category="category"/>
  <div class="threads">
    <div v-for="thread in threads" v-bind:key="thread.text">
      <SingleThread :thread="thread" :isOpen="false"/>
    </div>
  </div>
</template>

<style scoped>
.threads {
  display: flex;
  flex-direction: column;
  max-width: 1200px;
  margin: 50px auto;
  align-items: flex-start;
  gap: 30px;
}
</style>