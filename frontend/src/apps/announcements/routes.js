import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import AnnouncementsPage from "./views/AnnouncementsPage.vue";


export default [
    {
        path: "announcements/",
        component: AppTopBarLayout,
        meta: {
            getDisplayName: () => "Annnouncements",
            defaultRoute: "Announcements",
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
                name: "Announcement",
                props: true,
                meta: {
                    defaultRoute: "Announcement",
                    getDisplayName: () => "View"
                }
            }
        ]
    }
]