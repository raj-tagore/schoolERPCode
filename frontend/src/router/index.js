import { useAuthStore } from "@/stores/auth";
import { createRouter, createWebHistory } from "vue-router";

import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue";
// Layouts
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

import ClassroomPage from "@/views/ClassroomPage.vue";
import ClassroomsPage from "@/views/ClassroomsPage.vue";
import DashboardPage from "@/views/DashboardPage.vue";
// Pages
import HomePage from "@/views/HomePage.vue";
import LoginPage from "@/views/LoginPage.vue";
import SubjectPage from "@/views/SubjectPage.vue";

import api, { getClassroom } from "@/services/api";

const routes = [
    {
        path: "/",
        name: "Home",
        component: HomePage,
        // No meta required, no layout special requirements
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
        path: "/app/",
        component: DashboardLayout,
        children: [
            {
                path: "dashboard/",
                name: "Dashboard",
                component: DashboardPage,
                meta: { requiresAuth: true },
            },
            {
                path: "classrooms/",
                component: AppTopBarLayout,
                meta: {
                    requiresAuth: true,
                    getDisplayName: () => "Classroom",
                    defaultRoute: "Classrooms",
                },
                children: [
                    {
                        path: "",
                        name: "Classrooms",
                        component: ClassroomsPage,
                    },
                    {
                        path: ":classroomId/",
                        props: true,
                        component: EmptyLayout,
                        meta: {
                            getDisplayName: async (params) =>
                                (await getClassroom(params.classroomId)).name,
                            defaultRoute: "Classroom",
                        },
                        children: [
                            {
                                path: "",
                                name: "Classroom",
                                component: ClassroomPage,
                                props: true,
                            },
                            {
                                path: "subject/",
                                component: EmptyLayout,
                                meta: {
                                    getDisplayName: () => "Subject",
                                    defaultRoute: "Subject",
                                },
                                children: [
                                    {
                                        path: ":subjectId/",
                                        component: SubjectPage,
                                        name: "Subject",
                                        props: true,
                                        meta: {
											defaultRoute: "Subject",
                                            getDisplayName: async (params) =>
                                                (
                                                    await api.get(
                                                        `api/allocation/subjects/${params.subjectId}`,
                                                    )
                                                ).data.name,
                                        },
                                    },
                                ],
                            },
                        ],
                    },
                ],
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
