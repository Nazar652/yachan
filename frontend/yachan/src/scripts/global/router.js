import {createRouter, createWebHistory} from 'vue-router'
import Index from "@/components/main_components/IndexPage.vue";
import CategoryThreads from "@/components/threads/CategoryThreads.vue";
import ThreadPosts from "@/components/posts/ThreadPosts.vue";
import MainHeader from "@/components/headers/MainHeader.vue";
import MainFooter from "@/components/footers/MainFooter.vue";
import CommonHeader from "@/components/headers/CommonHeader.vue";
// import CommonFooter from "@/components/footers/CommonFooter.vue";
import NotFound from "@/components/main_components/NotFound.vue";
import AboutPage from "@/components/main_components/AboutPage.vue";

const routes = [
    {
        path: '/',
        name: 'main',
        components: {
            default: Index,
            header: MainHeader,
            footer: MainFooter
        }
    },
    {
        path: '/cat/:category',
        name: 'category',
        props: true,
        components: {
            default: CategoryThreads,
            header: CommonHeader,
            footer: MainFooter
        }
    },
    {
        path: '/cat/:category/:thread_id',
        name: 'thread',
        props: true,
        components: {
            default: ThreadPosts,
            header: CommonHeader,
            footer: MainFooter
        }
    },
    {
        path: '/about',
        name: 'about',
        components: {
            default: AboutPage,
            header: MainHeader,
            footer: MainFooter
        }
    },
    {
        path: '/:pathMatch(.*)*',
        redirect: '/not-found',
    },
    {
        path: '/not-found',
        name: 'notFound',
        components: {
            default: NotFound,
            header: CommonHeader,
            footer: MainFooter
        }
    }
]


export const router = createRouter({
    history: createWebHistory(),
    routes
})
