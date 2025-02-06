import ClassroomPage from "@/apps/classrooms/views/ClassroomPage.vue";
import EditClassroomPage from "@/apps/classrooms/views/EditClassroomPage.vue";
import CreateClassroomPage from "@/apps/classrooms/views/CreateClassroomPage.vue";
import ClassroomsPage from "@/apps/classrooms/views/ClassroomsPage.vue";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import { api } from "@/services/api";
import ClassroomAnnouncementsPage from "@/apps/classrooms/views/ClassroomAnnouncementsPage.vue";

export default [
    {
        path: "classrooms/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Classes",
            defaultRoute: "Classrooms",
            description: "View and manage classrooms",
            getMenu: () => [
                {
                    title: "All Classrooms",
                    to: { name: "Classrooms" },
                },
                {
                    title: "Create Classrooms",
                    to: { name: "CreateClassroom" },
                },
            ],
            icon: 'mdi-google-classroom',
        },
        children: [
            {
                path: "create/",
                name: "CreateClassroom",
                component: CreateClassroomPage,
                meta: {
                    getDisplayName: () => "Create Classrooms",
                    defaultRoute: "CreateClassroom",
                },
            },
            {
                path: "",
                name: "Classrooms",
                component: ClassroomsPage,
            },
            {
                path: ":classroomId/",
                props: true,
                component: EmptyLayout,
                meta: {
                    getDisplayName: async (props) =>
                        props
                            ? (
                                await api.get(
                                    `api/allocation/classrooms/${props.classroomId}`,
                                )
                            ).data.name
                            : "Classrooms",
                    defaultRoute: "Classrooms",
                    getMenu: (props) => [
                        {
                            title: "View Classroom",
                            to: { name: "Classroom", props },
                        },
                        {
                            title: "Edit Classroom",
                            to: { name: "EditClassroom", props },
                        },
                        {
                            title: "Announcements",
                            to: { name: "ClassroomAnnouncements", props },
                        },
                    ],
                },
                children: [
                    {
                        path: "",
                        props: true,
                        name: "Classroom",
                        component: ClassroomPage,
                    },
                    {
                        path: "edit/",
                        props: true,
                        name: "EditClassroom",
                        component: EditClassroomPage,
                    },
                    {
                        path: "announcements/",
                        props: true,
                        name: "ClassroomAnnouncements",
                        component: ClassroomAnnouncementsPage,
                        meta: {
                            getDisplayName: () => "Announcements",
                            defaultRoute: "ClassroomAnnouncements",
                        },
                    },
                ],
            },
        ],
    },
];
