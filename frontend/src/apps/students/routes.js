import AppSideBarLayout from "@/layouts/AppSideBarLayout.vue";
import BreadcrumbsLayout from "@/layouts/BreadcrumbsLayout.vue";
import StudentPage from "./views/StudentPage.vue";
import StudentsPage from "./views/StudentsPage.vue";
import { api } from "@/services/api";

export default [
    {
        path: "students/",
        component: AppSideBarLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Students",
            defaultRoute: "Students",
            description: "View and manage students",
            getMenu: (props) => [
                {
                    title: "View Students",
                    to: { name: "Students", params: props },
                },
            ],
        },
        children: [
            {
                path: "",
                component: StudentsPage,
                name: "Students",
            },
            {
                path: "",
                component: BreadcrumbsLayout,
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
                                    .data.user_details.full_name,
                            getMenu: (props) => [
                                {
                                    title: "View Student",
                                    to: { name: "Student", params: props },
                                },
                            ],
                        },
                    },
                ],
            },
        ],
    },
];
