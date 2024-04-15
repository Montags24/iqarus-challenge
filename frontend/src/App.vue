<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>

  </header>

  <RouterView />
</template>

<script>
import HomeView from './views/HomeView.vue';

export default {
  components: {
    HomeView,
  },
};
</script>
