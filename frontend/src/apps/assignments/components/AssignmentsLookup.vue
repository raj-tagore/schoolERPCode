<template>
	<v-card variant="flat">
		<v-card-title>
			<v-row>
				<v-col cols="12" md="4" lg="3">
					<v-text-field
						v-model="filters.title"
						label="Search by title"
						density="comfortable"
						hide-details
					></v-text-field>
				</v-col>
				<v-col cols="12" md="4" lg="3">
					<v-text-field
						v-model="filters.description"
						label="Search by description"
						density="comfortable"
						hide-details
					></v-text-field>
				</v-col>
				<v-col cols="12" md="4" lg="2">
					<ServerAutocomplete
						v-model="filters.classroom"
						:getInfo="getClassroomInfoFromObj"
						label="Filter by classroom"
						:fetch="getClassrooms"
						searchField="name"
					/>
				</v-col>
				<v-col cols="12" md="4" lg="2">
					<ServerAutocomplete
						v-model="filters.subject"
						:getInfo="getSubjectInfoFromObj"
						label="Filter by subject"
						:fetch="getSubjects"
						searchField="name"
					/>
				</v-col>
				<v-col cols="12" md="4" lg="2">
					<v-checkbox
						v-model="filters.is_active"
						label="Filter by Active"
						clearable
						hide-details
						density="comfortable"
					></v-checkbox>
				</v-col>
			</v-row>
		</v-card-title>
		<ResponsiveDataTable 
			:getToFunction="(item) => ( { name : 'Assignment', params: {assignmentId: item.id}} )" 
			:headers="headers" 
			:fetch="getAssignments" 
			:filters="filters"
      		:forceMobile="forceMobile"
    	/>
	</v-card>
</template>

<script setup>
import { getAssignments } from "@/apps/assignments/api.js";
import {
	getClassroomInfoFromObj,
	getClassrooms,
} from "@/apps/classrooms/api.js";
import { getSubjectInfoFromObj, getSubjects } from "@/apps/subjects/api.js";
import { onMounted, ref } from "vue";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import ServerAutocomplete from "@/components/ServerAutocomplete.vue";

const filters = ref({
	title: "",
	description: null,
	is_active: null,
	subject: null,
	classroom: null,
});

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

const assignments = ref([]);

const classrooms = ref([]);
const subjects = ref([]);

onMounted(async () => {
	classrooms.value = (await getClassrooms()).results;
	subjects.value = (await getSubjects()).results;
	// Don't fetch assignments on mount, start with empty table
	assignments.value = [];
});
</script>
