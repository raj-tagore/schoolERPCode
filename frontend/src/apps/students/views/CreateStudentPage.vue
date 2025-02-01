<template>
	<v-container>
		<FormCard
			title="Student"
			actionName="Create"
			:model="model"
			:action="createStudent"
		/>
	</v-container>
</template>

<script setup>
import { ref } from "vue";
import FormCard from "@/components/FormCard.vue";
import { createStudent } from "../api";

const model = ref([
	{
		label: "First Name",
		key: "first_name",
		type: "string",
	},
	{
		label: "Last Name",
		key: "last_name",
		type: "string",
	},
	{
		label: "E-Mail",
		key: "email",
		type: "string",
	},
	{
		label: "Is Active",
		key: "is_active",
		type: "boolean",
		defaultValue: true,
	},
	{
		label: "Is Approved",
		key: "is_approved",
		type: "boolean",
		defaultValue: false,
	},
]);
</script>
