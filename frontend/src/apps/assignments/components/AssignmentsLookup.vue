<template>
	<v-card variant="flat">
		<v-card-title>
			<FilterCard 
				v-model="filters"
				:filtersInfo="filtersInfo" 
			/>
		</v-card-title>
		<ResponsiveDataTable 
			:getToFunction="(item) => ({name: 'Assignment', params: {assignmentId: item.id}})" 
			:headers="headers" 
			:fetch="getAssignments" 
			v-model="filters"
      		:forceMobile="forceMobile"
    	/>
	</v-card>
</template>

<script setup>
import { ref } from "vue";
import { getAssignments } from "@/apps/assignments/api.js";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import FilterCard from "@/components/FilterCard.vue";

const filters = ref({
	title: "",
	description: "",
	classroom: null,
	subject: null,
	is_active: null,
});

const filtersInfo = ref([
	{
		label: "Search by title",
		type: "string",
		key: "title",
	},
	{
		label: "Search by description",
		type: "string",
		key: "description",
	},
	{
		label: "Filter by classroom",
		type: "classroom",
		key: "classroom",
	},
	{
		label: "Filter by subject",
		type: "subject",
		key: "subject",
	},
	{
		label: "Filter by active",
		type: "n_nary",
		key: "is_active",
		fetchOptions: () => [
			{ title: "Active", value: true },
			{ title: "Inactive", value: false },
			{ title: "All", value: null },
		],
	},
]);

const props = defineProps({
	forceMobile: {
		type: Boolean,
		default: false,
	},
});

// Properly parses the date string, Date() constructor doesn't work well with ISO strings
const formatDate = (dateString) =>
	Intl.DateTimeFormat("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
	}).format(Date.parse(dateString));

const headers = [
	{ title: "Title", key: "title" },
	{ title: "Release Date", key: "release_at", formatFunc: formatDate },
	{ title: "Due Date", key: "due_at", formatFunc: formatDate },
	{ title: "Subject", key: "subject_details", formatFunc: (item) => item.name },
	{ title: "Actions", key: "actions", sortable: false },
];
</script>
