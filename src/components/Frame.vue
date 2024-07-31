<template>
    <div class="mt-4 border-2 border-black p-10 rounded-lg text-black">
        <diV class="flex flex-wrap">
            <div className="sm:border-0 pb-2 mb-2 sm:pb-0 sm:mb-0 flex-auto">
                <div class="items-start">
                    <p className="text-2xl font-bold left-5 text-center">{{ title }}</p>
                    <img className=" h-24 w-24 border-2 rounded-full  border-black ml-auto mr-auto mt-4 sm:shrink-0"
                        src="https://png.pngtree.com/png-vector/20230626/ourmid/pngtree-cute-poop-emoticon-with-kiss-vector-png-image_7321310.png" />
                </div>
            </div>

            <div class="flex-auto">
                <p className="font-bold text-lg">{{ theme }}</p>
                <ul>
                    <li>· 【要吃什麼】CEO</li>
                    <li>· Premiere 3年經驗</li>
                    <li>· 14歲踏入健身領域</li>
                    <li>· 15歲開始創業</li>
                    <li>· 15加入區塊鏈世界</li>
                </ul>
            </div>

            <div class="flex-auto">
                <p className="font-bold text-lg">{{ theme2 }}</p>
                <ul>
                    <li>· 剪輯後製</li>
                    <li>· 街頭攝影</li>
                    <li>· 加密貨幣</li>
                    <li>· 區塊鏈</li>
                    <li>· 健身</li>
                </ul>
            </div>

            <div class="flex-auto">
                <p className="font-bold text-lg">{{ theme3 }}</p>
                <ul>
                    <li>· 名字：朱光昱</li>
                    <li>· 感情：單身</li>
                    <li>· 職業：CEO、剪輯師</li>
                    <li>· 地區：地球</li>
                </ul>
            </div>
        </div>
        <div class="mt-10">
            <p class="font-bold text-xl">自我介紹：</p>
            <p class="text-base mt-4">{{ Introduction }}</p>
        </div>
    </div>
</template>


<script>
export default {

    props: {
        title: {
            type: String,
            required: true
        },

        theme: {
            type: String,
            required: true
        },

        theme2: {
            type: String,
            required: true
        },

        theme3: {
            type: String,
            required: true
        },

        Introduction: {
            type: String,
            required: true
        }
    },
}
</script>
