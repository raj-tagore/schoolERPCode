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
		<!-- Mobile view: Cards -->
		<v-data-table-server
			class="d-md-none"
			:items-length="assignmentLen"
			:headers="mobileHeaders"
			:items="assignments"
			@update:options="fetchAssignments"
			:search="search"
			:loading="loading"
		>
			<template #headers={}></template>
			<template #item={item}>
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
		</v-data-table-server>
		<v-data-table-server
			class="d-none d-md-block"
			:items-length="assignmentLen"
			:headers="headers"
			:items="assignments"
			@update:options="fetchAssignments"
			:search="search"
			:loading="loading"
		>
			<template #item.release_at="{ item }">
				{{ formatDate(item.release_at) }}
			</template>
			<template #item.due_at="{ item }">
				{{ formatDate(item.due_at) }}
			</template>
			<template #item.subject_name="{ item }">
				{{  item.subject_name }}
			</template>
			<template #item.actions="{ item }">
				<v-btn
					icon="mdi-arrow-right"
					size="small"
					variant="outlined"
					:to="{name: 'Assignment', params: {assignmentId: item.id}}"
				></v-btn>
			</template>
		</v-data-table-server>

	</v-card>
</template>

<script setup>
import { getAssignments } from "@/apps/assignments/api.js";
import {
	getClassroomInfoFromObj,
	getClassrooms,
} from "@/apps/classrooms/api.js";
import { getSubjectInfoFromObj, getSubjects } from "@/apps/subjects/api.js";
import { onMounted, ref, watch } from "vue";

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

const mobileHeaders = [
	{ title: "", key: "id" },
];

const assignments = ref([]);

const classrooms = ref([]);
const subjects = ref([]);

const loading = ref(false);

const assignmentLen = ref(10);

const search = ref({});

watch(filters.value, (f) => {
	search.value = structuredClone(f);
});

const fetchAssignments = async ({ page, itemsPerPage, search }) => {
	loading.value = true;
	try {
		// Filter out falsy values
		const filterParams = Object.fromEntries(
			Object.entries(search)
				.filter(([_, value]) => value)
				.map(([key, value]) => {
					// I blame python and django
					if (typeof value === "boolean") {
						if (value) {
							return [key, "True"];
						}
						return [key, "False"];
					}
					return [key, value];
				}),
		);

		filterParams.limit = itemsPerPage ? itemsPerPage : 10;
		filterParams.offset = (page ? page - 1 : 0) * itemsPerPage;
		// Only fetch if at least one filter is active
		if (Object.keys(filterParams).length > 0) {
			console.log(filterParams);
			const assignmentsListing = await getAssignments(filterParams);
			assignmentLen.value = assignmentsListing.count;
			assignments.value = assignmentsListing.results;
		} else {
			assignments.value = []; // Clear the table when no filters
		}
	} catch (error) {
		console.error("Error fetching assignments:", error);
	} finally {
		loading.value = false;
	}
};

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
