<!-- src/components/Timeline.vue -->
<template>
  <div class="relative">
    <div
      class="absolute left-1/2 transform -translate-x-1/2 w-0.5 h-full bg-gradient-to-b from-indigo-300 via-purple-300 to-pink-300"
    ></div>
    <div
      v-for="(item, index) in items"
      :key="index"
      class="mb-16 flex justify-between items-center w-full"
      :class="{ 'flex-row-reverse': index % 2 !== 0 }"
    >
      <div class="w-5/12">
        <div
          class="bg-white p-6 rounded-lg shadow-xl transform transition-all duration-500 hover:scale-105 hover:shadow-2xl"
          :class="{ 'text-right': index % 2 === 0 }"
        >
          <h3 class="text-xl font-semibold text-indigo-600 mb-2">{{ item.title }}</h3>
          <p class="text-sm text-indigo-400 mb-3">{{ item.date }}</p>
          <p class="text-gray-600">{{ item.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Timeline",
  props: {
    items: Array,
  },
};
</script>
