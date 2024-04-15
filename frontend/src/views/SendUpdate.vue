<template>
  <section class="mt-12 mb-16 pt-4 bg-black">
    <form class="w-full max-w-lg flex flex-col" @submit.prevent>
      <div class="w-full px-3 mb-6 md:mb-0">
        <label class="block uppercase text-white text-md font-bold mb-2" for="grid-state">
          Category
        </label>
        <div class="relative">
          <select
            class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            id="grid-state" v-model="selectedForm">
            <option>Infrastructure</option>
            <option>Medical</option>
            <option>Security</option>
            <option>Logistics</option>
            <option>Environment</option>
            <option>Health</option>
            <option>Communication</option>
          </select>
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
            </svg>
          </div>
        </div>
      </div>
      <div v-if="selectedForm.toLowerCase() == 'infrastructure'">
        <InfrastructureForm @submitForm="submitForm"></InfrastructureForm>
      </div>
      <div v-else-if="selectedForm.toLowerCase() == 'security'">
        <SecurityForm @submitForm="submitForm"></SecurityForm>
      </div>
    </form>
  </section>
</template>

<script>
import InfrastructureForm from '../components/InfrastructureForm.vue'
import SecurityForm from '@/components/SecurityForm.vue';

export default {
  components: {
    InfrastructureForm,
    SecurityForm
  },
  data() {
    return {
      selectedForm: 'Infrastructure'
    };
  },
  methods: {
    handleOnlineStatus() {
      this.onLine = navigator.onLine;
    },
    submitForm(payload) {
      console.log(payload)
    }
  }
};
</script>

<style scoped></style>
