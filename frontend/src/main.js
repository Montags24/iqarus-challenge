import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import './index.css'
import { OhVueIcon, addIcons } from 'oh-vue-icons'

import { IoSend, FaMapMarkerAlt, FaUserAlt } from 'oh-vue-icons/icons'

addIcons(IoSend, FaMapMarkerAlt, FaUserAlt)

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.component('v-icon', OhVueIcon)
app.mount('#app')
