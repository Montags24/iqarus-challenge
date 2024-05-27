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
import { getAllItems, clearStore } from './stores/offlineWorker';

export default {
  components: {
    MobileNavBar,
    MobileHeader
  },
  data() {
    return {
      onLine: navigator.onLine,
      sessionJwt: ""
    }
  },
  watch: {
    // whenever onLine changes from false to true - try to send entries in IndexedDb
    // to server
    async onLine(newStatus) {
      try {
        if (newStatus) {
          const formEntries = this.parseFormEntriesToJson(await getAllItems("formEntries"))
          const sessionJwt = (await getAllItems("sessionJwt"))[0].sessionJwt
          if (formEntries) {
            const response = await this.apiSubmitOfflineForms(formEntries, sessionJwt)
            this.$toast.success(`Back online. ${response.forms.length} forms posted successfully`)
            await clearStore("formEntries")
          }
        }
      } catch (error) {
        console.log(error)
      }
    }
  },
  methods: {
    handleOnlineStatus() {
      this.onLine = navigator.onLine;
    },
    parseFormEntriesToJson(formEntries) {
      const formsToReturn = []
      for (let i = 0; i < formEntries.length; i++) {
        formsToReturn.push(JSON.parse(formEntries[i].payload))
      }
      console.log(formsToReturn)
      return formsToReturn
    },
    async apiSubmitOfflineForms(formEntries, sessionJwt) {
      "In apiSubmitOfflineForms"
      let domainOrigin = window.location.origin
      if (domainOrigin.slice(-5) == ":5173") {
        domainOrigin = domainOrigin.replace(":5173", ":5000")
      }

      console.log('In apiSubmitOfflineForms')
      const payload = { payload: formEntries }

      const request_options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${sessionJwt}`
        },
        body: JSON.stringify(payload)
      }

      const url = domainOrigin + `/api/forms/`

      try {
        const response = await fetch(url, request_options)
        if (!response.ok) {
          const errorData = await response.json() // Throw an error object containing both the status code and the error message
          throw {
            status: response.status,
            message: errorData.message || 'Network response was not ok'
          }
        }
        const apiObject = await response.json()
        return apiObject
      } catch (error) {
        // If the error object contains a status code, return it along with the error message
        if (error.status) {
          throw { status: error.status }
        } else {
          // Otherwise, just return the error message
          throw new Error('Failed to submit forms: ' + error.message)
        }
      }
    }
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
