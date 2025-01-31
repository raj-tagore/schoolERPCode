import ClassroomPage from "@/apps/classrooms/views/ClassroomPage.vue";
import EditClassroomPage from "@/apps/classrooms/views/EditClassroomPage.vue";
import CreateClassroomPage from "@/apps/classrooms/views/CreateClassroomPage.vue";
import ClassroomsPage from "@/apps/classrooms/views/ClassroomsPage.vue";
import AppSideBarLayout from "@/layouts/AppSideBarLayout.vue";
import BreadcrumbsLayout from "@/layouts/BreadcrumbsLayout.vue";
import { api } from "@/services/api";

export default [
    {
        path: "classrooms/",
        component: AppSideBarLayout,
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
                path: "view/:classroomId/",
                props: true,
                component: BreadcrumbsLayout,
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
                ],
            },
        ],
    },
];
