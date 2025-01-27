import AppTopBarLayout from "@/layouts/AppTopBarLayout.vue";
import AssignmentsPage from "./views/AssignmentsPage.vue"

export default [
	{
		path: "assignments/",
		content: AppTopBarLayout,
		meta: {
			getDisplayName: () => "Assignments",
			defaultRoute: "Assignments",
		},
		children: [
			{
				path: "",
				component: AssignmentsPage,
				name: "Assignments",
			},
		]
	}
]
