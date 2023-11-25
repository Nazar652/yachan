import { createApp } from 'vue'
import App from './App.vue'
import { router } from './scripts/global/router'


createApp(App).use(router).mount('#app')
