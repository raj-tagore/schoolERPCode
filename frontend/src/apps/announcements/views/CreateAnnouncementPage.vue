<template>
	<v-container>
		<FormCard
			title="Announcement"
			actionName="Create"
			:model="model"
			:action="createAnnouncement"
		/>
	</v-container>
</template>

<script setup>
import { ref } from "vue";
import FormCard from "@/components/FormCard.vue";
import { createAnnouncement } from "../api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";
import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import { getSubjects, getSubjectInfoFromObj } from "@/apps/subjects/api";

const model = ref([
	{
		label: "Title",
		key: "title",
		type: "string",
	},
	{
		label: "Description",
		key: "description",
		type: "longstring",
	},
	{
		label: "Priority",
		key: "priority",
		type: "string",
		defaultValue: "low",
	},
	{
		label: "Is Active",
		key: "is_active",
		type: "boolean",
		defaultValue: true,
	},
	{
		label: "Is School Wide",
		key: "is_school_wide",
		type: "boolean",
		defaultValue: false,
	},
	{
		label: "Signed By",
		key: "signed_by",
		type: "number",
		fetchOptions: getTeachers,
		fetchOptionsInfo: getTeacherInfoFromObj,
		searchField: "name",
	},
	{
		label: "Release Date",
		key: "release_at",
		type: "datetime",
	},
	{
		label: "Expiry Date",
		key: "expiry_at",
		type: "datetime",
	},
	{
		label: "Classrooms",
		key: "classrooms",
		type: "array",
		fetchOptions: getClassrooms,
		fetchOptionsInfo: getClassroomInfoFromObj,
		searchField: "name",
		defaultValue: [],
	},
	{
		label: "Subjects",
		key: "subjects",
		type: "array",
		fetchOptions: getSubjects,
		fetchOptionsInfo: getSubjectInfoFromObj,
		searchField: "name",
		defaultValue: [],
	},
	{
		label: "Attach File",
		key: "attached_file",
		type: "attachment",
		defaultValue: null,
	},
]);
</script>
