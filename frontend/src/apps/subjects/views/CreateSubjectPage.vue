<template>
	<v-container>
		<FormCard
			title="Subject"
			actionName="Create"
			:model="model"
			:action="createSubject"

		/>
	</v-container>
</template>

<script setup>
import { createSubject } from "@/apps/subjects/api";
import { ref } from "vue";

import FormCard from "@/components/FormCard.vue";

import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";

const model = ref([
	{
		label: "Name",
		key: "name",
		type: "string",
	},
	{
		label: "Classroom",
		key: "classroom",
		type: "number",
		fetchOptions: getClassrooms,
		fetchOptionsInfo: getClassroomInfoFromObj,
		searchField: "name",
	},
	{
		label: "Description",
		key: "description",
		type: "longstring",
	},
	{
		label: "Teacher",
		key: "teacher",
		type: "number",
		fetchOptions: getTeachers,
		fetchOptionsInfo: getTeacherInfoFromObj,
		searchField: "name",
	},
	{
		label: "Is Active",
		key: "is_active",
		type: "boolean",
	},
]);
</script>
