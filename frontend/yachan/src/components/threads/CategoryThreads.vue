<script setup>
import NewThread from "@/components/threads/NewThread.vue";
import fetchThreads from "@/scripts/threads/fetchThreads";
import {defineProps, onUnmounted, ref, watch} from "vue";
import SingleThread from "@/components/threads/SingleThread.vue";
import {hostname} from "@/scripts/global/globalVariables";
import {useRouter} from 'vue-router'
import fetchSingleCategory from "@/scripts/categories/fetchSingleCategory";
import PaginationComponent from "@/components/main_components/PaginationComponent.vue";
import isAuthenticated from "@/scripts/global/isAuthenticated";

const router = useRouter()

const props = defineProps(['category'])
const category = ref(props.category)
const cat = ref(null)
const threads = ref([])
const page = ref(Number(router.currentRoute.value.query.page) || 1)
const authenticated = ref(false)


async function getCategory() {
  cat.value = await fetchSingleCategory(category.value)
}

async function getThreads() {
  threads.value = await fetchThreads(category.value, page.value);
}

try {
  await getCategory()
  await getThreads()
} catch (e) {
  router.push({name: 'notFound'});
}

function webSocketConnect(cat) {
  const webSocket = new WebSocket(`ws://${hostname}/ws/category/${cat}/`)
  webSocket.onmessage = categoryUpdate
  return webSocket
}

let webSocket = webSocketConnect(category.value)

watch(() => props.category, async (newSlug) => {
  category.value = newSlug
  await getThreads()
  await getCategory()
  webSocket = webSocketConnect(category.value)
});

watch(() => router.currentRoute.value.query.page, async (newPage) => {
  page.value = Number(newPage)
  await getThreads()
})

authenticated.value = await isAuthenticated()


onUnmounted(() => {
  webSocket.close()
})

function categoryUpdate() {
  getThreads()
}
</script>

<template>
  <div v-if="cat !== null">
    <div class="category-header">
      <h1>{{ cat.name }}</h1>
      <p>{{ cat.description }}</p>
    </div>
    <div class="newThread">
      <NewThread :category="category"/>
    </div>
    <PaginationComponent :link_name="'category'" :params="{category: category}" :page="page"
                         :count="threads.count" :delim="5"/>

    <div class="threads">
      <div v-for="thread in threads.results" v-bind:key="thread.text">
        <SingleThread :thread="thread" :isOpen="false" :authenticated="authenticated"/>
      </div>
    </div>
    <PaginationComponent :link_name="'category'" :params="{category: category}" :page="page"
                         :count="threads.count" :delim="5"/>
  </div>
</template>

<style scoped>
.threads {
  display: flex;
  flex-direction: column;
  max-width: 1200px;
  margin: 50px auto;
  gap: 30px;
}
.newThread {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.category-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.category-header h1 {
  font-size: 2rem;
  color: #888;
  margin-bottom: 10px;
}

.category-header p {
  font-size: 1.2rem;
  color: #666;
}
</style>