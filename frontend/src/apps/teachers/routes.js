import EmptyLayout from "@/layouts/EmptyLayout.vue";
import TeachersPage from "./views/TeachersPage.vue";
import { api } from "@/services/api";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import TeacherPage from "./views/TeacherPage.vue";

export default [
    {
        path: "teachers/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Teachers",
            defaultRoute: "Teachers",
            description: "View and manage teachers",
            getMenu: (props) => [
                {
                    title: "View Teachers",
                    to: { name: "Teachers", params: props },
                },
            ],
            icon: 'mdi-account-tie',
        },
        children: [
            {
                path: "",
                component: TeachersPage,
                name: "Teachers",
            },
            {
                path: ":teacherId",
                props: true,
                component: TeacherPage,
                meta: {
                    defaultRoute: "Teacher",
                    getDisplayName: async (params) =>
                        (await api.get(`api/accounts/teachers/${params.teacherId}/`)).data
                            .user_details.full_name,
                    getMenu: (props) => [
                        {
                            title: "View Teacher",
                            to: { name: "Teacher", params: props },
                        },
                        {
                            title: "Edit Teacher",
                            to: { name: "EditTeacher", params: props },
                        },
                    ],
                    icon: 'mdi-account-tie',
                },
                children: [
                    {
						path: "",
                        component: EmptyLayout,
                        //component: StudentPage,
                        name: "Teacher",
                        props: true,
                    },
                    {
						path: "edit/",
                        component: EmptyLayout,
                        name: "EditTeacher",
                        props: true,
                    },
                ],
            },
        ],
    },
];
