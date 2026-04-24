import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/about', name: 'about', component: () => import('../views/AboutView.vue') },
    { path: '/results', name: 'results', component: () => import('../views/ResultsView.vue') },
    { path: '/results/:id', name: 'result-detail', component: () => import('../views/ResultDetailView.vue') },
    { path: '/members', name: 'members', component: () => import('../views/MembersView.vue') },
    { path: '/news', name: 'news', component: () => import('../views/NewsView.vue') },
    { path: '/news/:id', name: 'news-detail', component: () => import('../views/NewsDetailView.vue') },
  ],
  scrollBehavior() {
    return { top: 0 }
  },
})

export default router
