<template>
  <nav class="bg-black text-white font-bold">
    <div class="mx-auto px-2 sm:px-6 lg:px-5">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">

        </div>
        <div>

          <div class="flex flex-1 sm:items-stretch sm:justify-start">
            <div class="flex flex-shrink-0 items-center">
              <button @click="this.$router.push('/');">{{ title }}</button>
            </div>
          </div>
          <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
            v-for="i in navLink" :key="i.title">
            <div class="relative ml-3">
              <a :href="i.src">{{ i.title }}</a>
            </div>
          </div>
        </div>
      </div>

      <!--選單-->
      <div>
        <ul class="flex absolute right-10 top-5 cetabsolute space-x-4 ">
          <li>
            <button @click="this.$router.push('/')">Home</button>
          </li>
          <li>
            <button @click="this.$router.push('/About')">About</button>
          </li>
          <li>
            <button @click="this.$router.push('/Collection')">Collection</button>
          </li>
        </ul>
      </div>

      <div class="sm:hidden" id="mobile-menu" />
    </div>
  </nav>
</template>



<script>
export default {
  data() {
    return {
      title: 'ChenGuang',

    };
  },
}

</script>
