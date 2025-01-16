import EmptyLayout from "@/layouts/EmptyLayout.vue"
import SubjectPage from "@/apps/subjects/views/SubjectPage.vue"
import api from "@/services/api"
import SubjectsPage from "./views/SubjectsPage.vue"
import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue"

export default [
    {
        path: "subject/",
        component: AppTopBarLayout,
        meta: {
            getDisplayName: () => "Subjects",
            defaultRoute: "Subjects",
        },
        children: [
            {
                path: "",
                component: SubjectsPage,
                name: "Subjects"
            },
            {
                path: ":subjectId/",
                component: SubjectPage,
                name: "Subject",
                props: true,
                meta: {
                    defaultRoute: "Subject",
                    getDisplayName: async (params) =>
                        (await api.get(`api/allocation/subjects/${params.subjectId}`)).data.name,
                },
            },
        ],
    },
]