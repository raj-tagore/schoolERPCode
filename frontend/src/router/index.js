import { useAuthStore } from "@/stores/auth";
import { createRouter, createWebHistory } from "vue-router";
// Layouts
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import DashboardPage from "@/views/DashboardPage.vue";
// Pages
import HomePage from "@/views/HomePage.vue";
import LoginPage from "@/views/LoginPage.vue";
// Routes in Apps
import classroomsRoutes from "@/apps/classrooms/routes";
import subjectsRoutes from "@/apps/subjects/routes"
import usersRoutes from "@/apps/users/routes"

const routes = [
    {
        path: "/",
        name: "Home",
        component: HomePage,
    },
    {
        path: "/login",
        component: EmptyLayout,
        children: [
            {
                path: "",
                name: "Login",
                component: LoginPage,
            },
        ],
    },
    {
        path: "/app/",
        component: DashboardLayout,
        children: [
            {
                path: "dashboard/",
                name: "Dashboard",
                component: DashboardPage,
                meta: { requiresAuth: true },
            },
            ...classroomsRoutes,
            ...subjectsRoutes,
            ...usersRoutes,
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
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        const token = authStore.getAccess;
        if (!token) {
            return next({ name: "Login" });
        }
    }
    if (to.matched.some((record) => record.meta.requiresAccount)) {
        const account = authStore.getAccount;
        if (!account) {
            return next({ name: "register" });
        }
    }
    next();
});

export default router;
