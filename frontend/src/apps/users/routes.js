import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue"
import EmptyLayout from "@/layouts/EmptyLayout.vue"
import UsersPage from "./views/UsersPage.vue"
import StudentPage from "./views/StudentPage.vue"
import StudentsPage from "./views/StudentsPage.vue"

export default [
    {
        path: "users/",
        component: AppTopBarLayout,
        meta: {
            getDisplayName: () => "Users",
            defaultRoute: "Users"
        },
        children: [
            {
                path: "",
                component: UsersPage,
                name: "Users",
            },
            {
                path: "students",
                component: StudentsPage,
                name: "Students",
            },
            {
                path: "teachers",
                component: EmptyLayout,
                name: "Teachers",
            },
            {
                path: "parents",
                component: EmptyLayout,
                name: "Parents",
            },
            {
                path: "student/:studentId",
                component: StudentPage,
                name: "Student",
                props: true,
                meta: {
                    defaultRoute: "Student",
                    getDisplayName: async (params) => 
                    (await api.get(`api/students/${params.studentId}/`)).data.user.full_name,
                },
            },
        ],
    },
]