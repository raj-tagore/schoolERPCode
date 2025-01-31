import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

import AssignmentsPage from "./views/AssignmentsPage.vue";
import AssignmentPage from "./views/AssignmentPage.vue";
import EditAssignmentPage from "./views/EditAssignmentPage.vue"

export default [
    {
        path: "assignments/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            getDisplayName: () => "Assignments",
            defaultRoute: "Assignments",
            description: "View and manage assignments",
            getMenu: () => [
                {
                    title: "All Assignments",
                    to: { name: "Assignments" },
                },
            ],
        },
        children: [
            {
                path: "",
                component: AssignmentsPage,
                name: "Assignments",
            },
            {
                path: ":assignmentId/",
				component: EmptyLayout,
                props: true,
                meta: {
                    defaultRoute: "Assignment",
                    getDisplayName: () => "View",
                    getMenu: (props) => [
                        {
                            title: "View Assignment",
                            to: { name: "Assignment", props },
                        },
                        {
                            title: "Edit Assignment",
                            to: { name: "EditAssignment", props },
                        },
                    ],
                },
				children: [
					{
						path: "",
						component: AssignmentPage,
						name: "Assignment",
						props: true,
					},
					{
						path: "edit/",
						component: EditAssignmentPage,
						name: "EditAssignment",
						props: true,
					}
				]
            },
        ],
    },
];
