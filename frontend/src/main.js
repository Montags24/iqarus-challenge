import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ToastPlugin from 'vue-toast-notification'

import App from './App.vue'
import router from './router'
import './index.css'
import 'vue-toast-notification/dist/theme-default.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ToastPlugin, {
  // One of the options
  position: 'top-right',
  duration: 3000
})

app.mount('#app')
