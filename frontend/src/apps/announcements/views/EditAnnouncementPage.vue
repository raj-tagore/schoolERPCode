<template>
	<v-container>
		<FormCard
			v-if="announcement"
			title="Announcement"
			actionName="Update"
			:model="model"
			:action="handleUpdate"
		/>
	</v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import FormCard from "@/components/FormCard.vue";
import { getAnnouncement, updateAnnouncement } from "../api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";
import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import { getSubjects, getSubjectInfoFromObj } from "@/apps/subjects/api";

const props = defineProps({
	announcementId: {
		type: Number,
		required: true,
	},
});

const announcement = ref(null);

const formatDateForInput = (dateString) => {
	if (!dateString) return "";
	return new Date(dateString).toISOString().slice(0, 16);
};

const model = ref([
	{
		label: "Title",
		key: "title",
		type: "string",
	},
	{
		label: "Description",
		key: "description",
		type: "string",
	},
	{
		label: "Priority",
		key: "priority",
		type: "select",
		items: ['low', 'medium', 'high'],
	},
	{
		label: "Is Active",
		key: "is_active",
		type: "boolean",
	},
	{
		label: "Is School Wide",
		key: "is_school_wide",
		type: "boolean",
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
	},
	{
		label: "Subjects",
		key: "subjects",
		type: "array",
		fetchOptions: getSubjects,
		fetchOptionsInfo: getSubjectInfoFromObj,
		searchField: "name",
	},
]);

const handleUpdate = async (formData) => {
	try {
		await updateAnnouncement(props.announcementId, formData);
		return { success: true };
	} catch (error) {
		console.error("Failed to update announcement:", error);
		return { success: false, error };
	}
};

onMounted(async () => {
	announcement.value = await getAnnouncement(props.announcementId);
	// Update model with default values from the existing announcement
	model.value = model.value.map(field => ({
		...field,
		defaultValue: field.key === 'release_at' || field.key === 'expiry_at'
			? formatDateForInput(announcement.value[field.key])
			: announcement.value[field.key]
	}));
});
</script>
