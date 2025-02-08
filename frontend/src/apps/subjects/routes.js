import SubjectPage from "@/apps/subjects/views/SubjectPage.vue";
import EditSubjectPage from "@/apps/subjects/views/EditSubjectPage.vue";
import CreateSubjectPage from "@/apps/subjects/views/CreateSubjectPage.vue";
import { api } from "@/services/api";
import SubjectsPage from "./views/SubjectsPage.vue";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import SubjectAnnouncementsPage from "./views/SubjectAnnouncementsPage.vue";
import { getSubject } from "./api";

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
            icon: 'mdi-book-open-variant'
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
                    getDisplayName: async (props) => {
                        const subject = await getSubject(props.subjectId);
                        return `${subject.name} [${subject.classroom_details.name}]`;
                    },
                    getMenu: (props) => [
                        {
                            title: "View Subject",
                            to: { name: "Subject", props },
                        },
                        {
                            title: "Edit Subject",
                            to: { name: "EditSubject", props },
                        },
                        {
                            title: "Announcements",
                            to: { name: "SubjectAnnouncements", props },
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
                    {
                        path: "announcements/",
                        component: SubjectAnnouncementsPage,
                        name: "SubjectAnnouncements",
                        props: true,
                    },
                ],
            },
        ],
    },
];
