import { createRouter, createWebHistory } from 'vue-router'
import Index from "@/components/main_components/IndexPage.vue";
import CategoryThreads from "@/components/main_components/CategoryThreads.vue";
import ThreadPosts from "@/components/main_components/ThreadPosts.vue";
import MainHeader from "@/components/headers/MainHeader.vue";
import MainFooter from "@/components/footers/MainFooter.vue";
import CommonHeader from "@/components/headers/CommonHeader.vue";
import CommonFooter from "@/components/footers/CommonFooter.vue";

const routes = [
    {
        path: '/',
        components: {
            default: Index,
            header: MainHeader,
            footer: MainFooter
        }
    },
    {
        path: '/:category',
        components: {
            default: CategoryThreads,
            header: CommonHeader,
            footer: CommonFooter
        }
    },
    {
        path: '/:category/:thread_id',
        components: {
            default: ThreadPosts,
            header: CommonHeader,
            footer: CommonFooter
        }
    }
]

export const router = createRouter({
    history: createWebHistory(),
    routes
})
