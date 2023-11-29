<script setup>
import NewThread from "@/components/threads/NewThread.vue";
import fetchThreads from "@/scripts/threads/fetchThreads";
import {defineProps, onUnmounted, ref, watch} from "vue";
import SingleThread from "@/components/threads/SingleThread.vue";

const webSocket = new WebSocket('ws://127.0.0.1:8000/ws/threads')
webSocket.onmessage = handleNewThreadNotification

const props = defineProps(['category'])
const category = ref(props.category)

const threads = ref(null)

async function getThreads() {
  threads.value = await fetchThreads(category.value)
}

getThreads()

watch(() => props.category, async (newSlug) => {
  category.value = newSlug
  threads.value = await fetchThreads(category.value)
});

onUnmounted(() => {
  webSocket.close()
})

function handleNewThreadNotification(event) {
  const newThreadData = JSON.parse(event.data);
  if (newThreadData.data.category === category.value) {
    getThreads()
  }
}
</script>

<template>
  <NewThread :category="$route.params.category"/>
  <div class="threads">
    <div v-for="thread in threads" v-bind:key="thread.id" class="thread">
      <SingleThread :thread="thread"/>
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

.thread {
  padding: 20px;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  gap: 20px;
  background-color: wheat;
}
</style>