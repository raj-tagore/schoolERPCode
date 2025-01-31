import AppSideBarLayout from "@/layouts/AppSideBarLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import BreadcrumbsLayout from "@/layouts/BreadcrumbsLayout.vue";
import StudentPage from "./views/StudentPage.vue";
import StudentsPage from "./views/StudentsPage.vue";
import EditStudentsPage from "./views/EditStudentsPage.vue";
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
                {
                    title: "Edit Students",
                    to: { name: "EditStudents", params: props },
                },
            ],
        },
        children: [
            {
                path: "edit/",
                component: EditStudentsPage,
                name: "EditStudents",
            },
            {
                path: "",
                component: StudentsPage,
                name: "Students",
            },
            {
                path: ":studentId",
                props: true,
                component: BreadcrumbsLayout,
                meta: {
                    defaultRoute: "Student",
                    getDisplayName: async (params) =>
                        (await api.get(`api/accounts/students/${params.studentId}/`)).data
                            .user_details.full_name,
                    getMenu: (props) => [
                        {
                            title: "View Student",
                            to: { name: "Student", params: props },
                        },
                        {
                            title: "Edit Student",
                            to: { name: "EditStudent", params: props },
                        },
                    ],
                },
                children: [
                    {
						path: "",
                        component: StudentPage,
                        name: "Student",
                        props: true,
                    },
                    {
						path: "edit/",
                        component: EmptyLayout,
                        name: "EditStudent",
                        props: true,
                    },
                ],
            },
        ],
    },
];
