import EmptyLayout from "@/layouts/EmptyLayout.vue";
import ParentsPage from "./views/ParentsPage.vue";
import { api } from "@/services/api";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";


export default [
    {
        path: "parents/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Parents",
            defaultRoute: "Parents",
            description: "View and manage parents",
            getMenu: (props) => [
                {
                    title: "View Parents",
                    to: { name: "Parents", params: props },
                },
            ],
        },
        children: [
            {
                path: "",
                component: ParentsPage,
                name: "Parents",
            },
            {
                path: ":parentId",
                props: true,
                component: EmptyLayout,
                meta: {
                    defaultRoute: "Parent",
                    getDisplayName: async (params) =>
                        (await api.get(`api/accounts/parents/${params.parentId}/`)).data
                            .user_details.full_name,
                    getMenu: (props) => [
                        {
                            title: "View Parent",
                            to: { name: "Parent", params: props },
                        },
                        {
                            title: "Edit Parent",
                            to: { name: "EditParent", params: props },
                        },
                    ],
                },
                children: [
                    {
						path: "",
                        component: EmptyLayout,
                        //component: StudentPage,
                        name: "Parent",
                        props: true,
                    },
                    {
						path: "edit/",
                        component: EmptyLayout,
                        name: "EditParent",
                        props: true,
                    },
                ],
            },
        ],
    },
];
