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

const webSocket = new WebSocket(`ws://${hostname}/ws/category/${category.value}/`)
webSocket.onmessage = categoryUpdate


watch(() => props.category, (newSlug) => {
  category.value = newSlug
  getThreads()
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
  getThreads()
  makePagesArray()
}
</script>

<template>
  <div v-if="cat !== null">
    <NewThread :category="category"/>
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
  align-items: flex-start;
  gap: 30px;
}
</style>