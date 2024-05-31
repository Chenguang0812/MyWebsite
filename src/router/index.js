import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },

    {
      path: '/About',
      name: 'About',
      component: () => import('../views/About.vue')
    },
    {
      path: '/collection',
      name: 'collection',
      component: () => import('../views/Collection.vue')
    },
    {
      path: '/Introduction',
      name: 'Introduction',
      component: () => import('../About Me/Introduction.vue')
    },
    {
      path: '/Experience',
      name: 'Experience',
      component: () => import('../About Me/Experience.vue')
    },
    {
      path: '/Life_Growth_process',
      name: 'Life_Growth_process',
      component: () => import('../About Me/Life_Growth_process.vue')
    },
    {
      path: '/Found_The_Team',
      name: 'Found_The_Team',
      component: () => import('../About Me/Found_The_Team.vue')
    },
  ]
})

export default router
