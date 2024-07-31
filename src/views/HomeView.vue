<template>
  <div class="container mx-auto pt-8 pl-5 pr-5 dark:text-white transition-colors duration-100">
    <div class="text-3xl text-black font-bold">{{ title }}</div>
    <p class="text-base text-black no-underline leading-loose">一個15歲少年</p>
    <p class="text-base text-black no-underline">未來望可以成為企業家的一個人</p>
    <!--框框-->
    <div v-for="i in FrameData" :key="i.title">
      <Frame :title="i.title" :theme="i.theme" :theme2="i.theme2" :theme3="i.theme3" :Introduction="i.Introduction" />
    </div>
    <!--Timeline-->
    <br>
    <div class="home">
      <h1 class="text-2xl font-bold text-black text-center mb-6">我的時間軸</h1>
      <Timeline 
        v-for="(item, index) in timelineItems" 
        :key="index"
        :item="item"
      />
    </div>

  </div>
</template>

<script>
import Frame from '../components/Frame.vue'
import Timeline from '../components/Timeline.vue'
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
      timelineItems: [
        {
          title: '國二加入RC Studio',
          date: 'December, 2022 - Present',
          description: '對剪輯後製及各種社群媒體非常了解。',
          tags: ['剪輯後製', '社群媒體經營'],
        },
        {
          title: '國二開始接觸健身',
          date: 'December, 2022 - Present',
          description: '對於身體構造健身知識目前有一定的專業程度。',
          tags: ['健身', '重量訓練', '張力'],
        },
        {
          title: '國三接觸區塊鏈',
          date: 'May, 2023 - Present',
          description: '對於加密貨幣以及區塊鏈技術有著一定程度了解。',
          tags: ['區塊鏈技術', '加密貨幣', '交易'],
        },
        {
          title: '國三開始開創飲食App',
          date: 'January, 2024 - Present',
          description: '目前還在開創階段，只能說酷哦。',
          tags: ['要吃什麼', '我想吃屎'],
        },

      ],
    }
  },
  components: {
    Frame,
    Timeline,
  },
}
</script>
