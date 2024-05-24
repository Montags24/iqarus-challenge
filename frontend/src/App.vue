<script setup>
import { RouterView } from 'vue-router'
import { reactive } from 'vue';

import User from './stores/User';
import Maps from './stores/Maps';

// when we are developing using localhost on port 5173 (vue's default port),
// to integrate with the flask backend, we need to modify the port to 5000 (flask default port)
let domainOrigin = window.location.origin
if (domainOrigin.slice(-5) == ":5173") {
  domainOrigin = domainOrigin.replace(":5173", ":5000")
}

const user = reactive(new User(domainOrigin))
const maps = reactive(new Maps(domainOrigin, user))
</script>

<template>
  <div class="bg-black min-h-[calc(100vh-118px)]">
    <!-- Header -->
    <header class="relative z-10">
      <MobileHeader :onLine="onLine" :user="user"></MobileHeader>
    </header>

    <!-- Content -->
    <main class="relative z-0">
      <RouterView :onLine="onLine" :user="user" :maps="maps" />
    </main>

    <!-- Footer -->
    <footer class="relative z-10">
      <MobileNavBar :user="user"></MobileNavBar>
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
    this.$router.push('/profile')
  },
  beforeUnmount() {
    window.removeEventListener("online", this.handleOnlineStatus);
    window.removeEventListener("offline", this.handleOnlineStatus);
  },
};
</script>
