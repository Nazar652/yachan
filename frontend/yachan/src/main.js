import { createApp } from 'vue'
import App from './App.vue'
import { router } from './scripts/global/router'
import './assets/styles.css'


createApp(App)
    .mixin({
        inheritAttrs: false
})
    .use(router)
    .mount('#app')
