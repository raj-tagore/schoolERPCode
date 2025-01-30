import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue";
import AssignmentsPage from "./views/AssignmentsPage.vue"
import AssignmentPage from "./views/AssignmentPage.vue"

export default [
	{
		path: "assignments/",
		content: AppTopBarLayout,
		meta: {
			getDisplayName: () => "Assignments",
			defaultRoute: "Assignments",
			description: "View and manage assignments",
		},
		children: [
			{
				path: "",
				component: AssignmentsPage,
				name: "Assignments",
			},
            {
                path: ":assignmentId/",
                component: AssignmentPage,
                name: "Assignment",
                props: true,
                meta: {
                    defaultRoute: "Assignment",
                    getDisplayName: () => "View"
                }
            }
		]
	}
]
