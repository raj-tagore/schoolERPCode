<template>
	<v-container>
		<FormCard
			v-if="classroom"
			title="Classroom"
			actionName="Update"
			:model="model"
			:action="updateClassroom"
		/>
	</v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import FormCard from "@/components/FormCard.vue";
import { getClassroom, updateClassroom } from "../api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";

const props = defineProps({
	classroomId: {
		type: Number,
		required: true,
	},
});

const classroom = ref(null);

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
	},
]);

onMounted(async () => {
	classroom.value = await getClassroom(props.classroomId);
	// Update model with default values from the existing classroom
	model.value = model.value.map(field => ({
		...field,
		defaultValue: classroom.value[field.key]
	}));
});
</script>
