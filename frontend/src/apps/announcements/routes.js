import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue";
import AnnouncementsPage from "./views/AnnouncementsPage.vue";
import AnnouncementPage from "./views/AnnouncementPage.vue";

export default [
    {
        path: "announcements/",
        component: AppTopBarLayout,
        meta: {
            getDisplayName: () => "Annnouncements",
            defaultRoute: "Announcements",
            description: "View and manage announcements",
            getMenu: () => [
                {
                    title: "All Announcements",
                    to: { name: "Announcements" },
                },
            ],
        },
        children: [
            {
                path: "",
                component: AnnouncementsPage,
                name: "Announcements",
            },
            {
                path: ":announcementId/",
                component: AnnouncementPage,
                name: "Announcement",
                props: true,
                meta: {
                    defaultRoute: "Announcement",
                    getDisplayName: () => "View",
                    getMenu: (params) => [
                        {
                            title: "View Announcements",
                            to: { name: "Announcement", params },
                        },
                    ],
                },
            },
        ],
    },
];
