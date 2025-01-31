import SubjectPage from "@/apps/subjects/views/SubjectPage.vue";
import EditSubjectPage from "@/apps/subjects/views/EditSubjectPage.vue";
import { api } from "@/services/api";
import SubjectsPage from "./views/SubjectsPage.vue";
import AppSideBarLayout from "@/layouts/AppSideBarLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

export default [
    {
        path: "subjects/",
        component: AppSideBarLayout,
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
                component: EmptyLayout,
                meta: {
                    defaultRoute: "Subject",
                    getDisplayName: async (props) =>
                        (await api.get(`api/allocation/subjects/${props.subjectId}`)).data
                            .name,

                    getMenu: (props) => [
                        {
                            title: "View Subject",
                            to: { name: "Subject", props },
                        },
                    ],
                },
                children: [
                    {
                        path: "",
                        component: SubjectPage,
                        name: "Subject",
                        props: true,
                    },
                    {
                        path: "edit",
                        component: EditSubjectPage,
                        name: "EditSubject",
                        props: true,
                    },
                ],
            },
        ],
    },
];
