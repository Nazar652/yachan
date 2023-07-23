<template>
  <Suspense>
    <router-view name="header"></router-view>
  </Suspense>
  <div>
    <router-view></router-view>
  </div>
  <router-view name="footer"></router-view>

<!--  <Suspense>-->
<!--    <NewThread/>-->
<!--  </Suspense>-->
<!--  <GetThreads/>-->

</template>

<script>
  // import NewThread from "@/components/included_components/NewThread.vue";
  // import GetThreads from "@/components/GetThreads.vue";

  export default {
    name: 'App',
    components: {
      // GetThreads,
      // NewThread
    }
  }
</script>

<style>
  * {
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    background-color: lightblue;
  }
</style>
