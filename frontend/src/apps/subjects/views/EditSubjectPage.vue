<template>
	<v-container>
		<FormCard
			v-if="subject"
			title="Subject"
			actionName="Update"
			:model="model"
			:action="handleUpdate"
		/>
	</v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import FormCard from "@/components/FormCard.vue";
import { getSubject, updateSubject } from "../api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";

const props = defineProps({
	subjectId: {
		type: Number,
		required: true,
	},
});

const subject = ref(null);

const model = ref([
	{
		label: "Name",
		key: "name",
		type: "string",
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

const handleUpdate = async (formData) => {
	try {
		await updateSubject(props.subjectId, formData);
		return { success: true };
	} catch (error) {
		console.error("Failed to update subject:", error);
		return { success: false, error };
	}
};

onMounted(async () => {
	subject.value = await getSubject(props.subjectId);
	// Update model with default values from the existing subject
	model.value = model.value.map(field => ({
		...field,
		defaultValue: subject.value[field.key]
	}));
});
</script>
