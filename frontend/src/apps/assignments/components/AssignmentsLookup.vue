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
					<v-autocomplete
						v-model="filters.classroom"
						:items="classrooms"
						label="Filter by classroom"
						:item-props="getClassroomInfoFromObj"
						clearable
						hide-details
						density="comfortable"
					></v-autocomplete>
				</v-col>
				<v-col cols="12" md="4" lg="2">
					<v-autocomplete
						v-model="filters.subject"
						:items="subjects"
						label="Filter by subject"
						:item-props="getSubjectInfoFromObj"
						clearable
						hide-details
						density="comfortable"
					></v-autocomplete>
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
		<ResponsiveDataTable :headers="headers" :fetch="getAssignmentsListing" :filters="filters">
			<!--- Mobile template --->
			<template #mobile="{ item }">
				<v-card
					class="ma-2 pa-2"
					variant="outlined"
				>
					<div class="d-flex align-center justify-space-between">
						<v-card-title class="text-subtitle-1">{{ item.title }}</v-card-title>
						<v-btn
							icon="mdi-arrow-right"
							size="small"
							variant="outlined"
							:to="{name: 'Assignment', params: {assignmentId: item.id}}"
						></v-btn> 
					</div>
					<v-card-text>
						<div class="d-flex flex-column gap-1">
							<div class="d-flex align-center justify-space-between">
								<span class="text-caption">Release:</span>
								<span>{{ formatDate(item.release_at) }}</span>
							</div>
							<div class="d-flex align-center justify-space-between">
								<span class="text-caption">Expiry:</span>
								<span>{{ formatDate(item.due_at) }}</span>
							</div>
							<div class="d-flex align-center justify-space-between">
								<span class="text-caption">Subject:</span>
								<span>{{item.subject_name}}</span>
							</div>
						</div>
					</v-card-text>
				</v-card>
			</template>

			<!--- Desktop template --->
			<template #release_at="{ item }">
				{{ formatDate(item.release_at) }}
			</template>
			<template #due_at="{ item }">
				{{ formatDate(item.due_at) }}
			</template>
			<template #subject_name="{ item }">
				{{  item.subject_details.name }}
			</template>
			<template #actions="{ item }">
				<v-btn
					icon="mdi-arrow-right"
					size="small"
					variant="outlined"
					:to="{name: 'Assignment', params: {assignmentId: item.id}}"
				></v-btn>
			</template>
		</ResponsiveDataTable>
	</v-card>
</template>

<script setup>
import { getAssignmentsListing } from "@/apps/assignments/api.js";
import {
	getClassroomInfoFromObj,
	getClassrooms,
} from "@/apps/classrooms/api.js";
import { getSubjectInfoFromObj, getSubjects } from "@/apps/subjects/api.js";
import { onMounted, ref } from "vue";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";

const filters = ref({
	title: "",
	description: null,
	is_active: null,
	subject: null,
	classroom: null,
});

const headers = [
	{ title: "Title", key: "title" },
	{ title: "Release Date", key: "release_at" },
	{ title: "Due Date", key: "due_at" },
	{ title: "Subject", key: "subject_name" },
	{ title: "Actions", key: "actions", sortable: false },
];

const assignments = ref([]);

const classrooms = ref([]);
const subjects = ref([]);

// Properly parses the date string, Date() constructor doesn't work well with ISO strings
const formatDate = (dateString) =>
	Intl.DateTimeFormat("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
	}).format(Date.parse(dateString));

onMounted(async () => {
	classrooms.value = await getClassrooms();
	subjects.value = await getSubjects();
	// Don't fetch assignments on mount, start with empty table
	assignments.value = [];
});
</script>
