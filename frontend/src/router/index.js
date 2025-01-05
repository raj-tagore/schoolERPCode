import { useAuthStore } from '@/stores/auth'
import { createRouter, createWebHistory } from 'vue-router';

// Layouts
import DashboardLayout from '@/layouts/DashboardLayout.vue';
import EmptyLayout from '@/layouts/EmptyLayout.vue';

import DashboardPage from '@/views/DashboardPage.vue';
// Pages
import HomePage from '@/views/HomePage.vue';
import LoginPage from '@/views/LoginPage.vue';
import ClassroomPage from '@/views/ClassroomPage.vue';

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
  // {
  //   path: '/register',
  //   component: EmptyLayout,
  //   children: [
  //     {
  //       path: '',
  //       name: 'register',
  //       component: RegisterPage,
  //     },
  //   ],
  // },
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
    path: '/classroom',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Classroom',
        component: ClassroomPage,
        meta: { requiresAuth: true },
      },
      {
        path: '/join',
        name: 'Classroom Join',
        component: ClassroomPage,
        meta: { requiresAuth: true },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const token = authStore.getAccess;
    if (!token) {
      return next({ name: 'Login' });
    }
  }
  if (to.matched.some(record => record.meta.requiresAccount)) {
    const account = authStore.getAccount;
    if (!account) {
      return next({ name: 'register' });
    }
  }
  next();
});

export default router;
