<template>
  <div>
    <!-- Desktop Navbar (显示于大屏幕) -->
    <nav
      v-if="!isMobile"
      class="fixed top-0 left-0 right-0 bg-gradient-to-r from-blue-600 to-indigo-600 z-50 transition-all duration-300 ease-in-out shadow-lg"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex-shrink-0 w-1/4">
            <button
              class="text-white font-bold text-xl hover:text-blue-200 transition-colors duration-200"
              @click="navigateTo('/')"
            >
              {{ title }}
            </button>
          </div>

          <!-- Desktop navigation -->
          <div class="hidden xl:flex flex-grow justify-center w-1/2">
            <div class="flex items-center justify-center space-x-4">
              <button
                v-for="(item, index) in navItems"
                :key="item"
                class="text-white hover:bg-blue-700 px-3 py-2 rounded-md text-lg font-bold transition-colors duration-200"
                @click="navigateTo(navPaths[index])"
              >
                {{ item }}
              </button>
            </div>
          </div>

          <div class="flex-shrink-0 w-1/4 flex justify-end items-center">
            <div class="mr-2 xl:mr-0">
              <theme />
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Mobile Navbar and Sidebar -->
    <div v-if="isMobile">
      <!-- Mobile Navbar -->
      <div
        class="fixed top-0 left-0 right-0 bg-gradient-to-r from-blue-600 to-indigo-600 shadow-lg z-50"
      >
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex items-center justify-between h-16">
            <button
              class="text-white font-bold text-xl hover:text-blue-200 transition-colors duration-200"
              @click="navigateTo('/')"
            >
              {{ title }}
            </button>

            <button
              class="inline-flex items-center justify-center p-2 rounded-md text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white transition-colors duration-200"
              @click="toggleNavbar"
            >
              <span class="sr-only">Open main menu</span>
              <svg
                :class="{ hidden: isOpen, block: !isOpen }"
                class="h-6 w-6"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
              <svg
                :class="{ block: isOpen, hidden: !isOpen }"
                class="h-6 w-6"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Overlay -->
      <div
        v-if="isOpen"
        class="fixed inset-0 bg-black bg-opacity-50 z-40"
        @click="toggleNavbar"
      ></div>

      <!-- Mobile Sidebar -->
      <div
        :class="{ 'translate-x-0': isOpen, 'translate-x-full': !isOpen }"
        class="fixed top-0 right-0 bottom-0 w-64 bg-white shadow-xl overflow-y-auto transition-transform duration-300 ease-in-out z-50 rounded-l-3xl"
      >
        <div class="px-4 pt-20 pb-3 space-y-1">
          <button
            v-for="(item, index) in navItems"
            :key="item"
            class="text-gray-800 hover:bg-blue-100 block px-3 py-2 rounded-md text-base w-full text-left transition-colors duration-200"
            @click="navigateTo(navPaths[index])"
          >
            {{ item }}
          </button>
        </div>
      </div>
    </div>

    <!-- Main content wrapper -->
    <div class="transition-margin duration-300 ease-in-out">
      <!-- Your main content goes here -->
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
      title: "ChenGuang",
      navItems: ["Home", "About", "Collection"],
      navPaths: ["/", "/About", "/Collection"],
      isMobile: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.isOpen = !this.isOpen;
    },
    navigateTo(path) {
      this.$router.push(path);
      window.scrollTo(0, 0);
      if (this.isMobile) {
        this.isOpen = false;
      }
    },
    updateDevice() {
      this.isMobile = window.innerWidth < 1280;
    },
  },
  mounted() {
    this.updateDevice();
    window.addEventListener("resize", this.updateDevice);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.updateDevice);
  },
};
</script>
