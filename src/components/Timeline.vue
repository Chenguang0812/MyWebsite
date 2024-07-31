<!-- Timeline.vue -->
<template>
    <div class="relative max-w-3xl mx-auto px-4">
        <div class="absolute top-0 left-4 h-full w-0.5 bg-gray-300"></div>
      <div class="mb-8 ml-6">
        <!-- 點點 -->
        <div class="absolute w-3 h-3 bg-gray-500 rounded-full mt-1.5 -left-1.5 border border-white"></div>
        <div class="p-4 bg-white rounded-lg shadow">
          <h3 class="text-lg font-semibold text-gray-800 mb-1">{{ item.title }}</h3>
          <p v-if="item.date" class="text-sm text-gray-600 italic mb-2">{{ item.date }}</p>
          <p v-if="item.description" class="text-gray-700 mb-2">{{ item.description }}</p>
          <div v-if="item.tags" class="flex flex-wrap gap-2">
            <span v-for="(tag, tagIndex) in item.tags" :key="tagIndex"
                  class="px-2 py-1 bg-gray-100 text-gray-600 text-xs font-medium rounded">
              {{ tag }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      item: {
        type: Object,
        required: true
      }
    }
  }
  </script>