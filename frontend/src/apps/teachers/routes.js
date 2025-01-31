import EmptyLayout from "@/layouts/EmptyLayout.vue";

export default [
    {
        path: "teachers/",
        component: EmptyLayout,
        name: "Teachers",
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
        },
        children: [],
    },
];
