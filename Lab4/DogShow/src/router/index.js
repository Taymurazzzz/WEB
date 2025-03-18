import { createRouter, createWebHistory } from 'vue-router';
import MainPageView from '../views/MainPageView.vue';
import LoginPageView from '../views/LoginPageView.vue';
import ProfilePageView from '../views/ProfilePageView.vue';
import RegisterPageView from '@/views/RegisterPageView.vue';
import RegisterEventPageView from '@/views/RegisterEventPageView.vue';

const routes = [
  { path: '/', name: 'Home', component: MainPageView },
  { path: '/login', component: LoginPageView },
  { path: '/profile', component: ProfilePageView},
  {path: '/register', component: RegisterPageView},
  {path: '/registerforevent/:id', name: "RegisterEvent", component: RegisterEventPageView, props: true}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated');
  if (to.meta.requiresAuth && !isAuthenticated) {
    return '/login';
  }
});

export default router;