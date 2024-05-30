<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue'
import Navbar from './components/Navbar.vue'
</script>

<template>

  <Navbar />
    <div class="container mx-auto pt-8 pl-5 pr-5 text-black dark:text-white transition-colors duration-100">
      <RouterView />
      
    </div>
    <Footer />
    <br>
</template>
