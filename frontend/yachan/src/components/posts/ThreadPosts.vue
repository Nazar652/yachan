<script setup>
  import {defineProps, ref} from 'vue'
  import NewPost from "@/components/posts/NewPost.vue";

  const props = defineProps(['thread_id'])
  const threadId = ref(props.thread_id)
  const posts = ref(null)



</script>

<template>
  <NewPost :threadId="$route.params.thread_id"></NewPost>
</template>

<style scoped>

</style>