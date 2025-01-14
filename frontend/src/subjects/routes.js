import EmptyLayout from "@/layouts/EmptyLayout.vue"
import SubjectPage from "@/subjects/views/SubjectPage.vue"
import api from "@/services/api"

export default [
    {
        path: "subject/",
        component: EmptyLayout,
        meta: {
            getDisplayName: () => "Subject",
            defaultRoute: "Subject",
        },
        children: [
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