<script setup>
import {defineProps, ref, watchEffect} from 'vue'

const props = defineProps(['link_name', 'params', 'page', 'pages', 'pagesCount'])
const linkName = ref(props.link_name)
const params = ref(props.params)
const page = ref(props.page)
const pages = ref(props.pages)
const pagesCount = ref(props.pagesCount)

watchEffect(() => {
  linkName.value = props.link_name
  params.value = props.params
  page.value = props.page
  pages.value = props.pages
  pagesCount.value = props.pagesCount
});

</script>

<template>
  <div class="pages">
    <div class="pages-list">
      <div class="pagination-link pag-prev" v-if="page !== 1">
        <router-link :to="{ name: linkName, params: params, query: {page: page-1} }">&lt;
        </router-link>
      </div>
      <div class="pagination-link" v-for="pageNum in pages" :key="pageNum">
        <div v-if="pageNum !== 0" :class="{currentPage: Number(pageNum) === Number(page)}">
          <router-link :to="{ name: linkName, params: params, query: {page: pageNum} }">
            {{ pageNum }}
          </router-link>
        </div>
        <div v-else class="pag-placeholder">...</div>
      </div>
      <div class="pagination-link pag-next" v-if="page !== pagesCount">
        <router-link :to="{ name: linkName, params: params, query: {page: page+1} }">&gt;
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
a {
text-decoration: none;
color: black;
}

.pages-list {
display: flex
}

.pagination-link a, .pagination-link .pag-placeholder {
  padding: 5px 20px;
  border: 1px solid black;
  display: block;
  background-color: #f0f0f0;
}

.pagination-link:nth-child(1) a {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}

.pagination-link:nth-last-child(1) a {
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}


.currentPage a {
  background-color: #3498db;
  color: #fff
}

.pagination-link a:hover {
  background-color: #2980b9;
  color: #fff
}


</style>