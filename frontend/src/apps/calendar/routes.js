import CalendarPage from "@/apps/calendar/views/CalendarPage.vue";
import CalendarsPage from "@/apps/calendar/views/CalendarsPage.vue";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

export default [
    {
        path: "calendar/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            getDisplayName: () => "Calendar",
            defaultRoute: "Calendars",
            description: "View and manage calendars",
            getMenu: () => [
                {
                    title: "All Calendars",
                    to: { name: "Calendars" },
                }
            ],
            icon: 'mdi-calendar'
        },
        children: [
            {
                path: "",
                component: CalendarsPage,
                name: "Calendars",
            },
            {
                path: ":calendarId/",
                component: EmptyLayout,
                meta: {
                    defaultRoute: "Calendar",
                    getDisplayName: (props) => `Calendar View`,
                    getMenu: (props) => [
                        {
                            title: "View Calendar",
                            to: { name: "Calendar", props },
                        }
                    ],
                },
                children: [
                    {
                        path: "",
                        component: CalendarPage,
                        name: "Calendar",
                        props: true,
                    }
                ],
            },
        ],
    },
];
