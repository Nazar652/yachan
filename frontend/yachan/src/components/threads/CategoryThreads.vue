<script setup>
import NewThread from "@/components/threads/NewThread.vue";
import fetchThreads from "@/scripts/threads/fetchThreads";
import {defineProps, onUnmounted, ref, watch} from "vue";
import SingleThread from "@/components/threads/SingleThread.vue";
import {hostname} from "@/scripts/global/globalVariables";
import {useRouter} from 'vue-router'
import fetchSingleCategory from "@/scripts/categories/fetchSingleCategory";
import PaginationComponent from "@/components/main_components/PaginationComponent.vue";

const router = useRouter()

const props = defineProps(['category'])
const category = ref(props.category)
const cat = ref(null)
const threads = ref([])
const pages = ref([])
const page = ref(Number(router.currentRoute.value.query.page) || 1)
const pagesCount = ref(1)


async function getCategory() {
  cat.value = await fetchSingleCategory(category.value)
}

async function getThreads() {
  threads.value = await fetchThreads(category.value, page.value);
  pagesCount.value = Math.ceil(threads.value.count / 5)
}

try {
  await getCategory()
  await getThreads()
} catch (e) {
  router.push({name: 'notFound'});
}

function makePagesArray() {
  pages.value = []
  for (let i = 1; i <= pagesCount.value; i++) {
    if (i === 1 || i === pagesCount.value || (i >= page.value - 2 && i <= page.value + 2)) {
      pages.value.push(i)
    } else if (pages.value[pages.value.length - 1] !== 0) {
      pages.value.push(0)
    }
  }
}

makePagesArray()

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
  makePagesArray()
})

onUnmounted(() => {
  webSocket.close()
})

function categoryUpdate() {
  console.log('category update')
  getThreads()
  makePagesArray()
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
                         :pages="pages" :pages-count="pagesCount"/>

    <div class="threads">
      <div v-for="thread in threads.results" v-bind:key="thread.text">
        <SingleThread :thread="thread" :isOpen="false"/>
      </div>
    </div>
    <PaginationComponent :link_name="'category'" :params="{category: category}" :page="page"
                         :pages="pages" :pages-count="pagesCount"/>
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