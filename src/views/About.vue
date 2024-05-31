<template>
    <div class="text-black pl-5 mt-4">
        <h1 class="text-4xl mb-4">About Me</h1>
        <p class="text-lg">BOO! 這裡是晨光，我是「要吃什麼」的CEO，也在RC Studio擔任剪輯師一職。</p>

    </div>
    <div class="flex">
        <div class="pl-5 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 2xl:grid-cols-2 gap-4">
            <div v-for="i in CardData" :key="i.title">
                <Card :title="i.title" :descriptive="i.descriptive" :content="i.content" :page="i.page" />
            </div>

        </div>
    </div>
    <br>

</template>

<script>
import Card from '@/components/Card.vue';
export default {
    data() {
        return {
            CardData: [
                {
                    title: "介紹",
                    descriptive: "Introduction",
                    content: "嘿嘿!見鬼啦!",
                    page: "/Introduction"
                },
                {
                    title: "經歷",
                    descriptive: "Experience",
                    content: "嘿嘿!見鬼啦!",
                    page: "/Experience"
                },
                {
                    title: "成長路程",
                    descriptive: "Life_Growth_process",
                    content: "嘿嘿!見鬼啦!",
                    page: "/Life_Growth_process"
                },
                {
                    title: "創業",
                    descriptive: "Found_The_Team",
                    content: "嘿嘿!見鬼啦!",
                    page: "/Found_The_Team"
                },

            ],
        };
    },
    components: {
        Card,
    },
}
</script>