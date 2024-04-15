<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="bg-black">
    <!-- Header -->
    <header class="relative z-10">
      <div class="sm:hidden">
        <MobileHeader :onLine="onLine"></MobileHeader>
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
  data() {
    return {
      onLine: navigator.onLine
    }
  },
  methods: {
    handleOnlineStatus() {
      this.onLine = navigator.onLine;
    }
  },
  mounted() {
    window.addEventListener("online", this.handleOnlineStatus);
    window.addEventListener("offline", this.handleOnlineStatus);
  },
  beforeUnmount() {
    window.removeEventListener("online", this.handleOnlineStatus);
    window.removeEventListener("offline", this.handleOnlineStatus);
  }
};
</script>
