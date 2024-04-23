import { createRouter, createWebHistory } from 'vue-router'
import SendUpdate from '@/views/SendUpdate.vue'
const MapView = import('@/views/MapView.vue')
const UserProfile = import('@/views/UserProfile.vue')
const RegisterView = import('@/views/RegisterView.vue')

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
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    }
  ]
})

export default router
