<template>
  <TokenGenerator/>
  <Suspense>
    <router-view name="header"></router-view>
  </Suspense>
  <div class="wrapper">
    <Suspense>
      <router-view></router-view>
    </Suspense>
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

import TokenGenerator from "@/components/main_components/TokenGenerator.vue";

export default {
  name: 'App',
  components: {
    TokenGenerator
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

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
}
</style>
