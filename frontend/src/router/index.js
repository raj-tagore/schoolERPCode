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
import Classroom from '@/components/ClassroomPage.vue';
import CreateClassroom from '@/components/CreateClassroomPage.vue';
import Subject from '@/components/SubjectPage.vue';
import CreateSubject from '@/components/CreateSubjectPage.vue';
import Assessment from '@/components/AssessmentPage.vue';
import CreateAssessment from '@/components/CreateAssessmentPage.vue';
import Assignment from '@/components/AssignmentPage.vue';
import CreateAssignment from '@/components/CreateAssignmentPage.vue';
import Attendance from '@/components/AssignmentPage.vue';

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
  },
  {
    path: '/classroom',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Classroom',
        component: Classroom,
        meta: { requiresAuth: true },
      },
      {
        path: 'create',
        name: 'CreateClassroom',
        component: CreateClassroom,
        meta: { requiresAuth: true },
      }
    ],
  },
  {
    path: '/subject',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Subject',
        component: Subject,
        meta: { requiresAuth: true },
      },
      {
        path: 'create',
        name: 'CreateSubject',
        component: CreateSubject,
        meta: { requiresAuth: true },
      }
    ],
  },
  {
    path: '/assessment',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Assessment',
        component: Assessment,
        meta: { requiresAuth: true },
      },
      {
        path: 'create',
        name: 'CreateAssessment',
        component: CreateAssessment,
        meta: { requiresAuth: true },
      }
    ],
  },
  {
    path: '/assignment',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Assignment',
        component: Assignment,
        meta: { requiresAuth: true },
      },
      {
        path: 'create',
        name: 'CreateAssignment',
        component: CreateAssignment,
        meta: { requiresAuth: true },
      }
    ],
  },
  {
    path: '/attendance',
    component: DashboardLayout,
    children: [
      {
        path: '',
        name: 'Attendance',
        component: Attendance,
        meta: { requiresAuth: true },
      },
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
