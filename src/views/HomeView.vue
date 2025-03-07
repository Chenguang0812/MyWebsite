<!-- src/views/HomeView.vue -->
<template>
  <div
    class="min-h-screen bg-gradient-to-br from-indigo-100 via-purple-100 to-pink-100 text-gray-800 font-sans"
  >
    <!-- Hero -->
    <header class="relative h-screen flex items-center justify-center overflow-hidden">
      <!-- 內容區塊 -->
      <div class="text-center z-10 px-6">
        <h1
          class="text-5xl sm:text-7xl font-extrabold mb-4 text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 animate-gradient-x drop-shadow-lg"
        >
          晨光個人網站
        </h1>
        <p
          class="text-lg sm:text-2xl mb-8 text-gray-700 animate-fade-in animation-delay-300 tracking-wide"
        >
          失敗的原因是你自己<br />沒有人叫你放棄，叫你放棄的是你自己
        </p>
        <button
          @click="scrollToAbout"
          class="bg-indigo-600 text-white font-semibold py-3 px-10 rounded-full shadow-xl transition duration-300 ease-in-out transform hover:scale-110 hover:bg-indigo-700 focus:outline-none focus:ring-4 focus:ring-indigo-400 focus:ring-opacity-50 animate-fade-in animation-delay-600"
        >
          了解更多
        </button>
      </div>

      <!-- 背景效果 -->
      <div class="absolute inset-0 z-0">
        <div
          class="absolute inset-0 bg-gradient-to-br from-indigo-400 via-purple-300 to-pink-300 opacity-40"
        ></div>
        <div
          class="absolute inset-0 bg-gradient-to-t from-white to-transparent opacity-30"
        ></div>
        <svg
          class="absolute bottom-0 left-0 right-0"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 320"
        >
          <path
            fill="#ffffff"
            fill-opacity="1"
            d="M0,288L48,272C96,256,192,224,288,213.3C384,203,480,213,576,229.3C672,245,768,267,864,245.3C960,224,1056,160,1152,138.7C1248,117,1344,139,1392,149.3L1440,160L1440,320L1392,320C1344,320,   1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
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
            "外送平台 Founder / CEO",
            "影片剪輯與後製（Premiere 3 年經驗）",
            "13歲起專注於健身與運動科學研究",
            "14歲創立個人事業",
            "15歲研究區塊鏈技術與應用",
          ],
        },
        {
          title: "興趣",
          items: ["創業與建立商業模式", "影片剪輯", "區塊鏈技術", "街頭攝影", "健身"],
        },
        {
          title: "個人資料",
          items: ["暱稱：晨光", "感情狀態：單身", "職業：CEO、剪輯師", "地區：地球"],
        },
      ],
      introduction:
        "我是晨光，一名 15 歲的創業者與加密貨幣投資者，目前創立並擔任外送平台的創辦人兼執行長。我熱衷於經濟學、數學、新媒體、區塊鏈與投資，並以自我實現為人生核心，不斷突破自身極限，發揮最大潛能。我的選擇建立在利他主義之上 —— 透過創造價值優化市場環境，讓更多人受益。我致力於以實際行動解決問題，構建更高效、公平的體系。",
      timelineItems: [
        {
          title: "13歲加入RC Studio",
          date: "December, 2022 - Present",
          description: " 3年剪輯與後製經驗，能夠獨立製作高質影片。",
        },
        {
          title: "13歲開始接觸健身",
          date: "December, 2022 - Present",
          description: "深入研究運動科學與健身理論，並應用於實際訓練。",
        },
        {
          title: "14歲接觸區塊鏈",
          date: "May, 2023 - Present",
          description: "專注於區塊鏈技術，研究DApp、區塊鏈經濟模型。",
        },
        {
          title: "15歲開始開創外送平台",
          date: "January, 2024 - Present",
          description: "致力於打造外送三方共贏局面，打造良好外送環境。",
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
