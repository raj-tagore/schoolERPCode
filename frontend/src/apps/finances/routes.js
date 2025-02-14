import EmptyLayout from "@/layouts/EmptyLayout.vue";
import RecordsPage from "./views/RecordsPage.vue";
import { api } from "@/services/api";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import RecordPage from "./views/RecordPage.vue";

export default [
    {
        path: "records/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Records",
            defaultRoute: "Records",
            description: "View and manage records",
            getMenu: (props) => [
                {
                    title: "View Records",
                    to: { name: "Records", params: props },
                },
            ],
            icon: "mdi-credit-card-outline",
        },
        children: [
            {
                path: "",
                component: RecordsPage,
                name: "Records",
            },
            {
                path: ":recordId",
                props: true,
                component: EmptyLayout,
                meta: {
                    defaultRoute: "Record",
                    getDisplayName: async (params) =>
                        (await api.get(`api/finances/record/${params.recordId}/`)).data.id,
                    getMenu: (props) => [
                        {
                            title: "View Record",
                            to: { name: "Record", params: props },
                        },
                    ],
                    icon: "mdi-account-card-outline",
                },
                children: [
                    {
                        path: "",
                        component: RecordPage,
                        name: "Record",
                        props: true,
                    },
                    /*
                    {
                        path: "edit/",
                        component: EmptyLayout,
                        name: "EditTeacher",
                        props: true,
                    },
                    */
                ],
            },
        ],
    },
];
