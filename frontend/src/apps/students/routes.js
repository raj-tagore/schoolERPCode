import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import StudentPage from "./views/StudentPage.vue";
import StudentsPage from "./views/StudentsPage.vue";
import EditStudentsPage from "./views/EditStudentsPage.vue";
import CreateStudentPage from "./views/CreateStudentPage.vue";
import { api } from "@/services/api";

export default [
    {
        path: "students/",
        component: AppSideBarBreadcrumbsLayout,
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
                    title: "Create Student",
                    to: { name: "CreateStudent", params: props },
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
                path: "create/",
                component: CreateStudentPage,
                name: "CreateStudent",
            },
            {
                path: ":studentId",
                props: true,
                component: EmptyLayout,
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
                        component: EditStudentsPage,
                        name: "EditStudent",
                        props: true,
                    },
                ],
            },
        ],
    },
];
