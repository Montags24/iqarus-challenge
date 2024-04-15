<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<template>
  <div class="bg-black">
    <!-- Header -->
    <header class="relative z-10">
      <div class="sm:hidden">
        <MobileHeader></MobileHeader>
      </div>
    </header>

    <!-- Content -->
    <main class="relative z-0 max-container">
      <RouterView />
    </main>

    <!-- Footer -->
    <footer class="relative z-10">
      <div class="sm:hidden">
        <MobileNavBar></MobileNavBar>
      </div>
    </footer>
  </div>
</template>

<script>
import MobileNavBar from './components/MobileNavBar.vue';
import MobileHeader from './components/MobileHeader.vue'

export default {
  components: {
    MobileNavBar,
    MobileHeader
  },
};
</script>
