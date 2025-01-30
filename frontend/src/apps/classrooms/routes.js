import ClassroomPage from "@/apps/classrooms/views/ClassroomPage.vue";
import ClassroomsPage from "@/apps/classrooms/views/ClassroomsPage.vue";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { api } from "@/services/api";

export default [
    {
        path: "classrooms/",
        component: DashboardLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Classes",
            defaultRoute: "Classrooms",
			description: "View and manage classrooms",
        },
        children: [
            {
                path: "",
                name: "Classrooms",
                component: ClassroomsPage,
            },
            {
                path: ":classroomId/",
                props: true,
                name: "Classroom",
                component: ClassroomPage,
                meta: {
                    getDisplayName: async (params) =>
                        params ? (await api.get(`api/allocation/classrooms/${params.classroomId}`)).data.name : "Classrooms",
                    defaultRoute: "Classrooms",
                },
            },
        ],
    },
]
