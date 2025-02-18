import EventsPage from "./views/EventsPage.vue";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

export default [
    {
        path: "calendar/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            getDisplayName: () => "Calendar",
            defaultRoute: "Calendar",
            description: "View and manage calendar",
            getMenu: () => [
                {
                    title: "Calendar",
                    to: { name: "Calendar" },
                },
                {
                    title: "Events",
                    to: { name: "Events" },
                },
            ],
            icon: 'mdi-calendar'
        },
        children: [
            {
                path: "",
                component: EmptyLayout,
                name: "Calendar",
            },
            {
                path: "events/",
                component: EmptyLayout,
                meta: {
                    defaultRoute: "Events",
                    getDisplayName: () => "Events",
                },
                children: [
                    {
                        path: "",
                        component: EventsPage,
                        name: "Events",
                    },
                    {
                        path: ":eventId/",
                        component: EmptyLayout,
                        props: true,
                        meta: {
                            defaultRoute: "Event",
                            getDisplayName: () => "Event",
                        },
                        children: [
                            {
                                path: "",
                                component: EmptyLayout,
                                name: "Event",
                            }
                        ]
                    }
                ]
            },
        ],
    },
];
