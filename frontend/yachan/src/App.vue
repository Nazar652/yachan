<template>
  <TokenGenerator/>
  <Suspense>
    <router-view name="header"></router-view>
  </Suspense>
  <div class="wrapper">
    <div class="wrapper-inner">
      <Suspense>
        <router-view></router-view>
      </Suspense>
    </div>
  </div>
  <router-view name="footer"></router-view>
</template>

<script>
import TokenGenerator from "@/components/main_components/TokenGenerator.vue";

export default {
  name: 'App',
  components: {
    TokenGenerator
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
  background-color: #e0f0f8;
}

.wrapper-inner {
  max-width: 1200px;
  margin: 0 auto;
}

.wrapper {
  padding-bottom: 40px;
}
</style>
