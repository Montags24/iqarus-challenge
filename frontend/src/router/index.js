import { createRouter, createWebHistory } from 'vue-router'
import SendUpdate from '../views/SendUpdate.vue'
import MapView from '@/views/MapView.vue'
import UserProfile from '@/views/UserProfile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: SendUpdate
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/profile',
      name: 'profile',
      component: UserProfile
    }
  ]
})

export default router
