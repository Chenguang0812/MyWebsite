<template>
        <div class="flex justify-center">
            <div class="rounded-lg shadow-lg bg-white max-w-sm">
                <a href="#!">
                        <iframe width="385" height="240"
                            :src="link"
                            title="YouTube video player" frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                        </iframe>
                </a>
                <!-- 文字及按紐 -->
                <div class="p-6">
                    <h5 class="text-black text-xl mb-2">{{ title }}</h5>
                    <p class="text-black text-base mb-4">{{ Description }}</p>
                    <a class=" inline-block px-6 py-2.5 bg-black text-white text-xs uppercase rounded" :href="button">
                        Go Video
                    </a>
                </div>
            </div>
        </div>
</template>

<script>
export default {

    props: {
        link: {
            type: String,
            required: true
        },

        title: {
            type: String,
            required: true
        },

        Description: {
            type: String,
            required: true
        },

        button: {
            type: String,
            required: true
        },
    },
}
</script>