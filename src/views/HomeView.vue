<template>
  <div class="container mx-auto pt-8 pl-5 pr-5 text-black dark:text-white transition-colors duration-100">
    <div class="text-3xl text-black font-bold">{{ title }}</div>
    <p class="text-base no-underline text-black leading-loose">一個15歲少年</p>
    <p class="text-base no-underline text-black">未來望可以成為企業家的一個人</p>
    <!--框框-->
    <div v-for="i in FrameData" :key="i.title">
      <Frame :title="i.title" :theme="i.theme" :theme2="i.theme2" :theme3="i.theme3" :Introduction="i.Introduction" />
    </div>
  </div>
</template>

<script>
import Frame from '../components/Frame.vue'
export default {
  data() {
    return {
      title: '晨光個人網站',
      FrameData: [
        {
          title: '晨光ROALX',
          theme: "經歷",
          theme2: "興趣",
          theme3: "個人資料",
          Introduction: "我是一個15歲少年，專注於新媒體行業，目前正在開創一款飲食App，國中加入一家剪輯工作室。我自己對於任何事物都感到有興趣，也因為這樣，為我的人生帶來很多有趣的事情。我堅決我自己是要比別人快樂的，所以想趁年輕時，讓自己更努力，之後才可能比別人輕鬆。"
        },


      ],
    }
  },
  components: {
    Frame,
  },
}
</script>
