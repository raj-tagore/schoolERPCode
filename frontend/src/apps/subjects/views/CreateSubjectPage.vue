<template>
	<v-container>
		<CreateForm
			title="Subject"
			:model="model"
			:create="createSubject"
		/>

	</v-container>
</template>

<script setup>
import { createSubject } from "@/apps/subjects/api";
import { ref } from "vue";

import CreateForm from "@/components/CreateForm.vue";

import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";

const model = ref([
	{
		label: "Name",
		key: "name",
		type: "string",
	},
	{
		label: "Is Active",
		key: "is_active",
		type: "boolean",
	},
	{
		label: "Description",
		key: "description",
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
		label: "Teacher",
		key: "teacher",
		type: "number",
		fetchOptions: getTeachers,
		fetchOptionsInfo: getTeacherInfoFromObj,
		searchField: "name",
	},
]);
</script>
