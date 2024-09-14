<!-- src/components/InfoCard.vue -->
<template>
  <div
    class="bg-white rounded-xl shadow-lg overflow-hidden transform transition duration-300 hover:scale-105 hover:shadow-xl"
  >
    <div class="p-6">
      <h3 class="text-xl font-semibold text-gray-800 mb-4">{{ title }}</h3>
      <ul class="list-disc list-inside space-y-2">
        <li v-for="(item, index) in items" :key="index" class="text-gray-600">
          {{ item }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "InfoCard",
  props: {
    title: String,
    items: Array,
  },
};
</script>
