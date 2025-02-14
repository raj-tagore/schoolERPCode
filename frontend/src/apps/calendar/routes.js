import EventsPage from "@/apps/calendar/views/EventsPage.vue";
import EventPage from "@/apps/calendar/views/EventPage.vue";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

export default [
    {
        path: "events/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            getDisplayName: () => "Events",
            defaultRoute: "Events",
            description: "View and manage events",
            getMenu: () => [
                {
                    title: "All Events",
                    to: { name: "Events" },
                }
            ],
            icon: 'mdi-calendar'
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
                meta: {
                    defaultRoute: "Event",
                    getDisplayName: (props) => `Event View`,
                    getMenu: (props) => [
                        {
                            title: "View Event",
                            to: { name: "Event", props },
                        }
                    ],
                },
                children: [
                    {
                        path: "",
                        component: EventPage,
                        name: "Event",
                        props: true,
                    }
                ],
            },
        ],
    },
];
