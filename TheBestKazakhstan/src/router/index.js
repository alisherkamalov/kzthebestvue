import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import RegistrationView from '@/views/RegistrationView.vue';
import AuthorizationView from '@/views/AuthorizationView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/registration',
      name: 'registration',
      component: RegistrationView
    },
    {
      path: '/authorization',
      name: 'authorization',
      component: AuthorizationView
    }
  ]
});

export default router;

