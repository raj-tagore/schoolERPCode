<template>
	<v-container>
		<FormCard
			title="Classroom"
			actionName="Create"
			:model="model"
			:action="createClassroom"
		/>
	</v-container>
</template>

<script setup>
import { ref } from "vue";
import { createClassroom } from "@/apps/classrooms/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";
import { getStudents, getStudentInfoFromObj } from "@/apps/students/api";
import FormCard from "@/components/FormCard.vue";

const model = ref([
	{
		label: "Standard",
		key: "standard",
		type: "string",
	},
	{
		label: "Name",
		key: "name",
		type: "string",
	},
	{
		label: "Class Teacher",
		key: "class_teacher",
		type: "number",
		fetchOptions: getTeachers,
		fetchOptionsInfo: getTeacherInfoFromObj,
		searchField: "name",
	},
	{
		label: "Is Active",
		key: "is_active",
		type: "boolean",
		defaultValue: true,
	},
	{
		label: "Other Teachers",
		key: "other_teachers",
		type: "array",
		fetchOptions: getTeachers,
		fetchOptionsInfo: getTeacherInfoFromObj,
		searchField: "name",
		defaultValue: [],
	},
	{
		label: "Students",
		key: "students",
		type: "array",
		fetchOptions: getStudents,
		fetchOptionsInfo: getStudentInfoFromObj,
		searchField: "name",
		defaultValue: [],
	},
]);
</script>
