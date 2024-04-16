<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="bg-black">
    <!-- Header -->
    <header class="relative z-10">
      <MobileHeader :onLine="onLine"></MobileHeader>
    </header>

    <!-- Content -->
    <main class="relative z-0 max-container">
      <RouterView :onLine="onLine" />
    </main>

    <!-- Footer -->
    <footer class="relative z-10">
      <MobileNavBar></MobileNavBar>
    </footer>
  </div>
</template>

<script>
import MobileNavBar from './components/MobileNavBar.vue';
import MobileHeader from './components/MobileHeader.vue';
import { getAllItems } from './stores/offlineWorker';

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
  watch: {
    // whenever onLine changes from false to true - try to send cached entries to server
    async onLine(newStatus) {
      if (newStatus) {
        console.log("Back online")
        const items = await getAllItems()
        if (items) {
          for (let i = 0; i < items.length; i++) {
            console.log(items[i])
            console.log(JSON.parse(items[i].name.payload))
          }
        }
      }
    }
  },
  methods: {
    handleOnlineStatus() {
      this.onLine = navigator.onLine;
    },
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
