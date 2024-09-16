<!-- src/views/HomeView.vue -->
<template>
  <div
    class="min-h-screen bg-gradient-to-br from-indigo-100 via-purple-100 to-pink-100 text-gray-800 font-sans"
  >
    <!-- Hero -->
    <header class="relative h-screen flex items-center justify-center overflow-hidden">
      <div class="text-center z-10 px-4">
        <h1
          class="text-5xl sm:text-7xl font-extrabold mb-4 text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-pink-500 animate-gradient-x"
        >
          晨光個人網站
        </h1>
        <p
          class="text-xl sm:text-2xl mb-8 text-gray-600 animate-fade-in animation-delay-300"
        >
          一個15歲少年，未來企業家的夢想
        </p>
        <button
          @click="scrollToAbout"
          class="bg-indigo-600 text-white font-bold py-3 px-8 rounded-full transition duration-300 ease-in-out transform hover:scale-105 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 animate-fade-in animation-delay-600"
        >
          了解更多
        </button>
      </div>
      <div class="absolute inset-0 z-0">
        <div
          class="absolute inset-0 bg-gradient-to-br from-indigo-300 via-purple-300 to-pink-300 opacity-30"
        ></div>
        <svg
          class="absolute bottom-0 left-0 right-0"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 320"
        >
          <path
            fill="#ffffff"
            fill-opacity="1"
            d="M0,192L48,197.3C96,203,192,213,288,229.3C384,245,480,267,576,250.7C672,235,768,181,864,181.3C960,181,1056,235,1152,234.7C1248,235,1344,181,1392,154.7L1440,128L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
          ></path>
        </svg>
      </div>
    </header>

    <!-- About -->
    <section id="about" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold text-center text-indigo-600 mb-12">關於我</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
          <InfoCard v-for="(card, index) in infoCards" :key="index" v-bind="card" />
        </div>
        <div
          class="bg-gradient-to-r from-indigo-50 to-purple-50 p-8 rounded-2xl shadow-xl relative overflow-hidden transform hover:scale-105 transition-all duration-300"
        >
          <div
            class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-indigo-500 to-purple-500"
          ></div>
          <h3 class="text-2xl font-semibold mb-6 text-indigo-600">自我介紹</h3>
          <p class="text-gray-700 leading-relaxed text-lg relative z-10">
            {{ introduction }}
          </p>
        </div>
      </div>
    </section>

    <!-- Timeline -->
    <section
      id="timeline"
      class="py-20 bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold text-center text-indigo-600 mb-12">我的時間軸</h2>
        <Timeline :items="timelineItems" />
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";
import InfoCard from "@/components/InfoCard.vue";
import Timeline from "@/components/Timeline.vue";

export default {
  name: "HomeView",
  components: {
    InfoCard,
    Timeline,
  },
  setup() {
    const scrollToAbout = () => {
      const aboutSection = document.getElementById("about");
      if (aboutSection) {
        aboutSection.scrollIntoView({ behavior: "smooth" });
      }
    };

    return {
      scrollToAbout,
      infoCards: [
        {
          title: "經歷",
          items: [
            "【要吃什麼】CEO",
            "Premiere 3年經驗",
            "14歲踏入健身領域",
            "15歲開始創業",
            "15歲加入區塊鏈世界",
          ],
        },
        {
          title: "興趣",
          items: ["剪輯後製", "街頭攝影", "加密貨幣", "區塊鏈", "健身"],
        },
        {
          title: "個人資料",
          items: ["暱稱：晨光", "感情：單身", "職業：CEO、剪輯師", "地區：地球"],
        },
      ],
      introduction:
        "我是一個15歲少年，專注於新媒體行業，目前正在開創一款飲食App，國中加入一家剪輯工作室。我自己對於任何事物都感到有興趣，也因為這樣，為我的人生帶來很多有趣的事情。我堅決我自己是要比別人快樂的，所以想趁年輕時，讓自己更努力，之後才可能比別人輕鬆。",
      timelineItems: [
        {
          title: "國二加入RC Studio",
          date: "December, 2022 - Present",
          description: "對剪輯後製及各種社群媒體非常了解。",
        },
        {
          title: "國二開始接觸健身",
          date: "December, 2022 - Present",
          description: "對於身體構造健身知識目前有一定的專業程度。",
        },
        {
          title: "國三接觸區塊鏈",
          date: "May, 2023 - Present",
          description: "對於加密貨幣以及區塊鏈技術有著一定程度了解。",
        },
        {
          title: "國三開始開創飲食App",
          date: "January, 2024 - Present",
          description: "目前還在開創階段，只能說酷哦。",
        },
      ],
    };
  },
};
</script>

<style scoped>
@keyframes gradient-x {
  0%,
  100% {
    background-size: 200% 200%;
    background-position: left center;
  }
  50% {
    background-size: 200% 200%;
    background-position: right center;
  }
}
.animate-gradient-x {
  animation: gradient-x 3s ease infinite;
}
.animate-fade-in {
  animation: fadeIn 1s ease-out;
}
.animation-delay-300 {
  animation-delay: 300ms;
}
.animation-delay-600 {
  animation-delay: 600ms;
}
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.special-cursor-area {
  cursor: url("/special-cursor.cur"), auto;
}
</style>
