<template>
  <div>
    <h1>Home View</h1>
    {{ counter }}
    <button>Increase counter</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      onLine: navigator.onLine,
      counter: 0
    }
  },
  methods: {
    increaseCount() {
      if (!this.onLine) {
        this.counter++
      }
    }
  },

}
</script>

<style scoped></style>