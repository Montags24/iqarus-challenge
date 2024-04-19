<template>
  <section class="mt-12 mb-16 pt-4">
    <form class="w-full max-w-lg mx-auto flex flex-col" @submit.prevent>
      <div class="w-full px-3 mb-6">
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
      <BoilerplateForm :formObj="loadForm()" @submitForm="submitForm"></BoilerplateForm>
    </form>
  </section>
</template>

<script>
import BoilerplateForm from '../components/BoilerplateForm.vue';
import { infrastructureForm, securityForm, communicationsForm } from '../components/index';
import { addItem, removeItem, getAllItems } from '@/stores/offlineWorker';
import { checkLocationPermission } from '@/stores/geoLocation';

export default {
  components: {
    BoilerplateForm,
  },
  props: {
    onLine: {
      type: Boolean,
    },
  },
  data() {
    return {
      infrastructureForm: infrastructureForm,
      securityForm: securityForm,
      communicationsForm: communicationsForm,
      selectedForm: 'Infrastructure',
      items: []
    };
  },
  methods: {
    submitForm(payload) {
      if (this.onLine) {
        console.log(`I am online! ${payload}`)
        checkLocationPermission()
      } else {
        this.addItemToDb(JSON.stringify(payload))
      }
    },
    async addItemToDb(payload) {
      try {
        const newItem = { payload };
        const itemId = await addItem(newItem);
        this.items.push({ id: itemId, ...newItem });
        console.log("added item")
      } catch (error) {
        console.error(error);
        alert('Failed to add item');
      }
    },
    loadForm() {
      switch (this.selectedForm.toLowerCase()) {
        case 'infrastructure':
          return this.infrastructureForm
        case 'security':
          return this.securityForm
        case 'communication':
          return this.communicationsForm
        default:
        // code block
      }
    }
  }
};
</script>

<style scoped></style>
