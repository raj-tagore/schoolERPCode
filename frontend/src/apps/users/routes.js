import AppSideBarLayout from "@/layouts/AppSideBarLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import StudentPage from "./views/StudentPage.vue";
import StudentsPage from "./views/StudentsPage.vue";
import { api } from "@/services/api";

export default [
    {
        path: "users/",
        component: AppSideBarLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Users",
            defaultRoute: "Users",
            description: "View and manage users",
            getMenu: () => [
                {
                    title: "All Students",
                    to: { name: "Students" },
                },
                {
                    title: "All Teachers",
                    to: { name: "Teachers" },
                },
                {
                    title: "All Parents",
                    to: { name: "Parents" },
                },
            ],
        },
        children: [
            {
                path: "",
                component: EmptyLayout,
                name: "Users",
            },
            {
                path: "students",
                component: StudentsPage,
                name: "Students",
            },
            {
                path: "teachers",
                component: EmptyLayout,
                name: "Teachers",
            },
            {
                path: "parents",
                component: EmptyLayout,
                name: "Parents",
            },
            {
                path: "students",
                component: EmptyLayout,
                name: "Students",
                meta: {
                    defaultRoute: "Students",
                    getDisplayName: async () => "Students",
                },
                children: [
                    {
                        path: ":studentId",
                        component: StudentPage,
                        name: "Student",
                        props: true,
                        meta: {
                            defaultRoute: "Student",
                            getDisplayName: async (params) =>
                                (await api.get(`api/accounts/students/${params.studentId}/`))
                                    .data.user.full_name,
                            getMenu: (params) => [
                                {
                                    title: "View Student",
                                    to: { name: "Student", params },
                                },
                            ],
                        },
                    },
                ],
            },
        ],
    },
];
