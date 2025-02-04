import EmptyLayout from "@/layouts/EmptyLayout.vue";
import CreateAttachmentPage from "./views/CreateAttachmentPage.vue";
import { api } from "@/services/api";
import AppSideBarBreadcrumbsLayout from "@/layouts/AppSideBarBreadcrumbsLayout.vue";


export default [
    {
        path: "attachments/",
        component: AppSideBarBreadcrumbsLayout,
        meta: {
            requiresAuth: true,
            getDisplayName: () => "Attachments",
            defaultRoute: "Attachments",
            description: "View and manage attachments",
            getMenu: (props) => [
                {
                    title: "View Attachments",
                    to: { name: "Attachments", params: props },
                },
                {
                    title: "Create Attachments",
                    to: { name: "CreateAttachment", params: props },
                },
            ],
            icon: 'mdi-paperclip',
        },
        children: [
            {
                path: "create/",
                name: "CreateAttachment",
                component: CreateAttachmentPage,
                meta: {
                    getDisplayName: () => "Create Attachment",
                    defaultRoute: "CreateAttachment",
                },
            },
            {
                path: "",
                component: EmptyLayout,
                name: "Attachments",
            },
            {
                path: ":parentId",
                props: true,
                component: EmptyLayout,
                meta: {
                    defaultRoute: "Attachment",
                    getDisplayName: async (params) =>
                        (await api.get(`api/accounts/parents/${params.parentId}/`)).data
                            .user_details.full_name,
                    getMenu: (props) => [
                        {
                            title: "View Attachment",
                            to: { name: "Attachment", params: props },
                        },
                        {
                            title: "Edit Attachment",
                            to: { name: "EditAttachment", params: props },
                        },
                    ],
                },
                children: [
                    {
						path: "",
                        component: EmptyLayout,
                        name: "Attachment",
                        props: true,
                    },
                    {
						path: "edit/",
                        component: EmptyLayout,
                        name: "EditAttachment",
                        props: true,
                    },
                ],
            },
        ],
    },
];
