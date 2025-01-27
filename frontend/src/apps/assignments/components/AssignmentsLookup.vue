<template>
	<v-card variant="flat">
		<v-card-title>
			<v-row>
				<v-col cols="12" md="4" lg="3">
					<v-text-field
						v-model="filters.title"
						label="Search by title"
						density="comfortable"
						@input="fetchAssignments"
						hide-details
					></v-text-field>
				</v-col>
				<v-col cols="12" md="4" lg="3">
					<v-text-field
						v-model="filters.description"
						label="Search by description"
						density="comfortable"
						@input="fetchAssignments"
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
						@update:model-value="fetchAssignments"
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
						@update:model-value="fetchAssignments"
						hide-details
						density="comfortable"
					></v-autocomplete>
				</v-col>
				<v-col cols="12" md="4" lg="2">
					<v-checkbox
						v-model="filters.is_active"
						label="Filter by Active"
						clearable
						@update:model-value="fetchAssignments"
						hide-details
						density="comfortable"
					></v-checkbox>
				</v-col>
			</v-row>
		</v-card-title>
		<!-- Mobile view: Cards -->
		<div class="d-md-none">
			<v-card
				v-for="item in assignments"
				:key="item.id"
				class="ma-2 pa-2"
				variant="outlined"
			>
				<div class="d-flex align-center justify-space-between">
					<v-card-title class="text-subtitle-1">{{ item.title }}</v-card-title>
					<v-btn
						icon="mdi-arrow-right"
						size="small"
						variant="outlined"
					></v-btn> <!-- Add router link -->
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
							<span>{{ subjects.filter((s) => s.id === item.subject)[0].name }}</span>
						</div>
					</div>
				</v-card-text>
			</v-card>
		</div>
		<v-data-table
			class="d-none d-md-block"
			:headers="headers"
			:items="assignments"
			:loading="loading"
		>
			<template #item.release_at="{ item }">
				{{ formatDate(item.release_at) }}
			</template>
			<template #item.due_at="{ item }">
				{{ formatDate(item.due_at) }}
			</template>
			<template #item.subject="{ item }">
				{{  subjects.filter((s) => s.id === item.subject)[0].name }}
			</template>
			<template #item.actions="{ item }">
				<v-btn
					icon="mdi-arrow-right"
					size="small"
					variant="outlined"
				></v-btn><!-- Add router link -->
			</template>
		</v-data-table>

	</v-card>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getAssignments } from "@/apps/assignments/api.js";
import {
	getClassrooms,
	getClassroomInfoFromObj,
} from "@/apps/classrooms/api.js";
import { getSubjects, getSubjectInfoFromObj } from "@/apps/subjects/api.js";

const filters = ref({
	title: "",
	description: null,
	is_active: null,
	subject: null,
	classroom: null,
});

const assignments = ref([]);

const classrooms = ref([]);
const subjects = ref([]);

const loading = ref(false);

const fetchAssignments = async () => {
	loading.value = true;
	try {
		// Filter out falsy values
		const filterParams = Object.fromEntries(
			Object.entries(filters.value)
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

		// Only fetch if at least one filter is active
		if (Object.keys(filterParams).length > 0) {
			console.log(filterParams);
			assignments.value = await getAssignments(filterParams);
		} else {
			assignments.value = []; // Clear the table when no filters
		}
	} catch (error) {
		console.error("Error fetching assignments:", error);
	} finally {
		loading.value = false;
	}
};

const formatDate = (dateString) => {
	// Properly parses the date string, Date() constructor doesn't work well with ISO strings
	return Intl.DateTimeFormat("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
	}).format(Date.parse(dateString));
};

onMounted(async () => {
	classrooms.value = await getClassrooms();
	subjects.value = await getSubjects();
	// Don't fetch assignments on mount, start with empty table
	assignments.value = [];
});
</script>
