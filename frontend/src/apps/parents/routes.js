import EmptyLayout from "@/layouts/EmptyLayout.vue";

export default [
    {
        path: "parents/",
        component: EmptyLayout,
        name: "Parents",
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
        children: [],
    },
];
