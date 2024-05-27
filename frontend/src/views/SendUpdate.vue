<template>
  <section class="mt-12 mb-16 pt-4">
    <form class="w-full max-w-lg mx-auto flex flex-col" @submit.prevent>
      <div class="w-full px-3 mb-6">
        <label class="block uppercase text-white text-md font-bold mb-2" for="grid-state">
          Category
        </label>
        <div class="relative">
          <select
            class="shadow bg-black text-white appearance-none border border-gray-700 rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            id="grid-state" v-model="selectedForm">
            <option>Infrastructure</option>
            <option>Medical</option>
            <option>Security</option>
            <option>Logistics</option>
            <option>Environment</option>
            <option>Health</option>
            <option>Communications</option>
          </select>
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-white">
            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
            </svg>
          </div>
        </div>
      </div>
      <BoilerplateForm :formObj="selectedFormObj" @submitForm="submitForm"></BoilerplateForm>
    </form>
  </section>
</template>

<script>
import BoilerplateForm from '../components/BoilerplateForm.vue';
import { infrastructureForm, securityForm, communicationsForm } from '../components/index';
import { addItem } from '@/stores/offlineWorker';
import { checkLocationPermission } from '@/stores/geoLocation';

export default {
  components: {
    BoilerplateForm,
  },
  props: {
    user: {
      type: Object,
    },
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
    async submitForm(payload) {
      if (navigator.onLine) {
        if (!this.user.loggedIn) {
          this.$router.push('/profile')
          this.$toast.info('Please login to post update')
        }
        try {
          payload = await this.addUserLocationToPayload(payload)
          console.log(payload)
          await this.user.apiSubmitForm(this.selectedForm.toLowerCase(), payload)
          this.$toast.success("Form successfully submitted")
        } catch (error) {
          console.log(error.status)
          if (error.status === 401) {
            this.$toast.warning('Please login first')
          } else {
            // Handle other errors
            console.log("Other error:", error);
          }
        }
      } else {
        try {
          payload = await this.addUserLocationToPayload(payload);
          await this.addItemToDb(JSON.stringify(payload));
          this.$toast.success('Form saved. Will attempt to send when back online');
        } catch (error) {
          console.error('Failed to save form offline:', error);
          this.$toast.error('Failed to save form offline');
        }
      }
    },
    async addUserLocationToPayload(payload) {
      try {
        const userPosition = await checkLocationPermission();
        payload.latitude = userPosition.coords.latitude
        payload.longitude = userPosition.coords.longitude
        payload.timestamp = Date.now()
        return payload
      } catch (error) {
        console.error('Error getting location:', error);
        // Handle error
      }
    },
    async addItemToDb(payload) {
      try {
        console.log(`The payload is ${payload}`)
        const newItem = { payload };
        const itemId = await addItem(newItem, "formEntries");
        this.items.push({ id: itemId, ...newItem });
      } catch (error) {
        console.error(error);
        alert('Failed to add item');
      }
    },
  },
  computed: {
    selectedFormObj() {
      switch (this.selectedForm.toLowerCase()) {
        case 'infrastructure':
          return this.infrastructureForm;
        case 'security':
          return this.securityForm;
        case 'communications':
          return this.communicationsForm;
        default:
          return null; // or handle the default case
      }
    }
  }
};
</script>

<style scoped></style>
