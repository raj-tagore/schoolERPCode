import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store';

// Layouts
import DashboardLayout from '@/layouts/DashboardLayout.vue';
import EmptyLayout from '@/layouts/EmptyLayout.vue';

// Pages
import HomePage from '@/views/HomePage.vue';
import LoginPage from '@/views/LoginPage.vue';
import DashboardPage from '@/views/DashboardPage.vue';
import AllClassroomsPage from '@/views/AllClassroomsPage.vue';
import SingleClassroomPage from '@/views/SingleClassroomPage.vue';
import CreateClassroomPage from '@/views/CreateClassroomPage.vue';

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
    path: '/classrooms',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'AllClassrooms',
        component: AllClassroomsPage,
        meta: { requiresAuth: true },
      },
      {
        path: 'create',
        name: 'CreateClassroom',
        component: CreateClassroomPage,
        meta: { requiresAuth: true },
      },
      {
        path: ':id',
        name: 'SingleClassroom',
        component: SingleClassroomPage,
        meta: { requiresAuth: true },
      }
    ],
  },
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
