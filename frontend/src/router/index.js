import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store';

// Layouts
import DashboardLayout from '@/layouts/DashboardLayout.vue';
import EmptyLayout from '@/layouts/EmptyLayout.vue';

// Pages
import HomePage from '@/components/HomePage.vue';
import LoginPage from '@/components/LoginPage.vue';
import RegisterPage from '@/components/RegisterPage.vue';
import DashboardPage from '@/components/DashboardPage.vue';
import Announcement from '@/components/AnnouncementPage.vue';
import CreateAnnouncement from '@/components/CreateAnnouncementPage.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
    // No meta required, no layout special requirements
  },
  {
    path: '/login',
    component: EmptyLayout,
    children: [
      {
        path: '',
        name: 'Login',
        component: LoginPage,
      },
    ],
  },
  {
    path: '/register',
    component: EmptyLayout,
    children: [
      {
        path: '',
        name: 'Register',
        component: RegisterPage,
        meta: { requiresAuth: true },
      },
    ],
  },
  {
    path: '/dashboard',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: DashboardPage,
        meta: { requiresAuth: true },
      },
    ],
  },
  {
    path: '/announcement',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Announcement',
        component: Announcement,
        meta: { requiresAuth: true },
      },
      {
        path: 'create',
        name: 'CreateAnnouncement',
        component: CreateAnnouncement,
        meta: { requiresAuth: true },
      }
    ],
  }

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const token = store.getters.access;
    if (!token) {
      return next({ name: 'Login' });
    }
  }
  next();
});

export default router;
