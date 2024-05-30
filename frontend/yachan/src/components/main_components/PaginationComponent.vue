<script setup>
import {defineProps, ref, watchEffect} from 'vue'

const props = defineProps(['link_name', 'params', 'page', 'count', 'delim'])
const linkName = ref(props.link_name)
const params = ref(props.params)
const page = ref(props.page)
const pagesCount = ref(null)
const count = ref(props.count)
const delim = ref(props.delim)
const pages = ref([])

function makePagesArray() {
  pages.value = []
  pagesCount.value = Math.ceil(count.value / delim.value)
  for (let i = 1; i <= pagesCount.value; i++) {
    if (i === 1 || i === pagesCount.value || (i >= page.value - 2 && i <= page.value + 2)) {
      pages.value.push(i)
    } else if (pages.value[pages.value.length - 1] !== 0) {
      pages.value.push(0)
    }
  }
}

makePagesArray()
watchEffect(() => {
  linkName.value = props.link_name
  params.value = props.params
  page.value = props.page
  count.value = props.count
  delim.value = props.delim
  makePagesArray()
});
</script>

<template>
  <div class="pages" v-if="pagesCount>0">
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