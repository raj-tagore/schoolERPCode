import SubjectPage from "@/apps/subjects/views/SubjectPage.vue";
import { api } from "@/services/api";
import SubjectsPage from "./views/SubjectsPage.vue";
import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue";

export default [
    {
        path: "subjects/",
        component: AppTopBarLayout,
        meta: {
            getDisplayName: () => "Subjects",
            defaultRoute: "Subjects",
            description: "View and manage subjects",
            getMenu: () => [
                {
                    title: "All Subjects",
                    to: { name: "Subjects" },
                },
            ],
        },
        children: [
            {
                path: "",
                component: SubjectsPage,
                name: "Subjects",
            },
            {
                path: ":subjectId/",
                component: SubjectPage,
                name: "Subject",
                props: true,
                meta: {
                    defaultRoute: "Subject",
                    getDisplayName: async (params) =>
                        (await api.get(`api/allocation/subjects/${params.subjectId}`)).data
                            .name,

                    getMenu: (params) => [
                        {
                            title: "View Subject",
                            to: { name: "Subject", params },
                        },
                    ],
                },
            },
        ],
    },
];
