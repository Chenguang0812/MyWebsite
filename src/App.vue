<template>
  <Navbar />

  <RouterView />

  <Footer />
  <br />
</template>

<script setup>
import { RouterView } from "vue-router";
import Footer from "./components/Footer.vue";
import Navbar from "./components/Navbar.vue";
</script>
<style>
body {
  cursor: url("/gam1564.cur"), auto;
}

/* 对于可点击元素，保持默认的指针样式 */
a,
button,
[role="button"],
input[type="submit"],
input[type="button"],
input[type="reset"] {
  cursor: pointer;
}

input[type="text"],
textarea {
  cursor: text;
}
</style>
