<template>
  <div>
    <h1>Home View</h1>
    <p v-if="onLine">Online</p>
    <p v-else>Offline</p>
    {{ counter }}
    <button @click="increaseCount">Increase counter</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      onLine: navigator.onLine,
      counter: 0
    };
  },
  methods: {
    increaseCount() {
      if (!this.onLine) {
        this.counter++;
      }
    },
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

<style scoped></style>
