import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue";
import UsersPage from "./views/UsersPage.vue";
import UserPage from "./views/UserPage.vue";
import api from '@/services/api';

export default [
    {
        path: "users/",
        component: AppTopBarLayout,
        meta: {
            getDisplayName: () => "Users",
            defaultRoute: "Users",
        },
        children: [
            {
                path: "",
                name: "Users",
                component: UsersPage,
            },
            {
                path: ":userId",
                component: UserPage,
                name: "User",
                props: true,
                meta: {
                    defaultRoute: "User",
                    getDisplayName: async (params) =>
                        (await api.get(`api/users/${params.userId}/`)).data.full_name,
                },
            },
        ],
    },
];
