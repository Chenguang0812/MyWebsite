<template>
    <div class="mt-4 border-2 border-black w-72 h-96 rounded-lg">
        <h1 class="text-black text-xl ml-3 mt-2 font-bold">{{ title }}</h1>
        <h2 class="text-black text-xs ml-3 font-bold">{{ descriptive }}</h2>
        <p class="text-black text-sm ml-3 mt-2">{{ content }}</p>
        <a :href="page" target="_blank">
            <button type="button" class="text-white bg-black focus:ring-4 rounded-lg text-xs px-5 py-2.5 mt-56 ml-3">
                查看更多
            </button>
        </a>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        descriptive: {
            type: String,
            required: true
        },
        content: {
            type: String,
            required: true
        },
        page: {
            type: String,
            required: true
        }

    }
}
</script>