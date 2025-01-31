import AppSideBarLayout from "@/layouts/AppSideBarLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

import AnnouncementsPage from "./views/AnnouncementsPage.vue";
import AnnouncementPage from "./views/AnnouncementPage.vue";
import EditAnnouncementPage from "./views/EditAnnouncementPage.vue";

export default [
    {
        path: "announcements/",
        component: AppSideBarLayout,
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
                component: EmptyLayout,
                props: true,
                meta: {
                    defaultRoute: "Announcement",
                    getDisplayName: () => "View",
                    getMenu: (params) => [
                        {
                            title: "View Announcement",
                            to: { name: "Announcement", params },
                        },
                        {
                            title: "Edit Announcement",
                            to: { name: "EditAnnouncement", params },
                        },
                    ],
                },
                children: [
                    {
                        path: "",
                        component: AnnouncementPage,
                        name: "Announcement",
                        props: true,
                    },
                    {
                        path: "edit/",
                        component: EditAnnouncementPage,
                        name: "EditAnnouncement",
                        props: true,
                    },
                ],
            },
        ],
    },
];
