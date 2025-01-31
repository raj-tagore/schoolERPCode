import { useAuthStore } from "@/stores/auth";
import { createRouter, createWebHistory } from "vue-router";
// Layouts
import DashboardBreadcrumbsLayout from "@/layouts/DashboardBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
// Pages
import HomePage from "@/views/HomePage.vue";
import LoginPage from "@/views/LoginPage.vue";
import DashboardPage from "@/views/DashboardPage.vue";
import AllAppsPage from "@/views/AllAppsPage.vue";
// Routes in Apps
import appRoutes from "@/router/app";

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
        component: DashboardBreadcrumbsLayout,
        children: [
			{
                path: "",
                name: "All Apps",
                component: AllAppsPage,
                meta: { requiresAuth: true },
			},
            {
                path: "dashboard/",
                name: "Dashboard",
                component: DashboardPage,
                meta: { requiresAuth: true },
            },
			...appRoutes,
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
