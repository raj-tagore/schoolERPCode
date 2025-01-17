import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue"
import EmptyLayout from "@/layouts/EmptyLayout.vue"
import UsersPage from "./views/UsersPage.vue"

export default [
    {
        path: "users/",
        component: AppTopBarLayout,
        name: "Users",
        meta: {
            getDisplayName: () => "Users",
            defaultRoute: "Users"
        },
        children: [
            {
                path: "",
                component: UsersPage
            },
            {
                path: ":userId",
                component: EmptyLayout,
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
]