<template>
    <div class="text-black text-center">
        <h1 class="mb-5 text-3xl font-bold leading-tight md:text-5xl md:leading-tight">
            剪輯作品集
        </h1>
        <h3 class="mb-5 text-3xl  leading-tight md:text-xl md:leading-tight">
            從事剪輯行業2年，對剪輯相當有熱枕，有著一定的創造力及想像力，<br/>剪過遊戲類、生活類等影片，目前任職於RC Studio擔任剪輯師。
        </h3>
        <br>
    </div>
    <div class="grid grid-cols-1 2xl:grid-cols-3 md:grid-cols-2 gap-5 sm:grid-cols-1">
        <div v-for="i in ytcardData" :key="i.link">
            <ytcard :link="i.link" :title="i.title" :Description="i.Description" />
        </div>
    </div>
    <br>
    <br>
</template>

<script>
import ytcard from '../components/ytcard.vue'
export default {
    data() {
        return {
            ytcardData: [
                {
                    link: 'https://www.youtube.com/embed/k2_3Ka3_IEw?si=ZD0XGX17JLe-gRCI&amp;controls=0',
                    title: "反骨柔柔",
                    Description: "公開超渣前男友!!各位姐妹小心👻手機裡竟然都是跟別人的影片...😨",
                },
                {
                    link: 'https://www.youtube.com/embed/LWL2i_uW7do?si=gLJPmd4DgZx3sdaT&amp;controls=0',
                    title: "雪兔",
                    Description: "【空之要塞：啟航】創新跑酷與射擊玩法一定要來體驗！！",
                },
                {
                    link: 'https://www.youtube.com/embed/7H7rtiTh4m0?si=_-BjDHIiJbh-Iez7&amp;controls=0',
                    title: "小妞",
                    Description: "我被床戰隊友陷害了，哈哈哈哈哈哈哈哈哈哈哈哈哈",
                },
                {
                    link: 'https://www.youtube.com/embed/_HHXvDfXfug?si=Pl1WQDx1zsXWFPNQ&amp;controls=0',
                    title: "ROALX",
                    Description: "你可以只用輪盤上轉到的槍枝獲得勝利嗎？？？？",
                },
                {
                    link: 'https://www.youtube.com/embed/fzngN3zOWHU?si=iymtoDCF0haqdFBS&amp;controls=0',
                    title: "RY",
                    Description: "【RY】不存在的樓層？嚇到螢幕都在抖！| 蛋仔派對",
                },
                {
                    link: 'https://www.youtube.com/embed/0iDJ7agNpsc?si=D3vJE5v8F8-g04mH&amp;controls=0',
                    title: "WuWei無為",
                    Description: "一部精華告訴你為什麼這遊戲還沒倒！各種混亂不堪但又好笑好玩的環境就是我們要的啦！",
                },
            ]
        };
    },
    components: {
        ytcard,
    },
}

</script>