import SubjectPage from "@/apps/subjects/views/SubjectPage.vue";
import EditSubjectPage from "@/apps/subjects/views/EditSubjectPage.vue";
import CreateSubjectPage from "@/apps/subjects/views/CreateSubjectPage.vue";
import { api } from "@/services/api";
import SubjectsPage from "./views/SubjectsPage.vue";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

export default [
    {
        path: "subjects/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            getDisplayName: () => "Subjects",
            defaultRoute: "Subjects",
            description: "View and manage subjects",
            getMenu: () => [
                {
                    title: "All Subjects",
                    to: { name: "Subjects" },
                },
                {
                    title: "Create Subject",
                    to: { name: "CreateSubject" },
                },
            ],
        },
        children: [
            {
                path: "create/",
                name: "CreateSubject",
                component: CreateSubjectPage,
                meta: {
                    getDisplayName: () => "Create Subject",
                    defaultRoute: "CreateClassroom",
                },
            },
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
                        {
                            title: "Edit Subject",
                            to: { name: "EditSubject", props },
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
                        path: "edit/",
                        component: EditSubjectPage,
                        name: "EditSubject",
                        props: true,
                    },
                ],
            },
        ],
    },
];
