<script setup>
import * as uuid from "uuid";
import {getToken, setToken} from "@/scripts/global/tokenUtils";
if (!getToken()) {
  setToken(uuid.v4())
}
</script>

<template>
<div></div>
</template>

<style scoped>

</style>