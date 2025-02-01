<template>
	<v-container>
		<v-card variant="flat">
			<v-card-title>
				<!-- Search filters -->
				<v-row>
					<v-col cols="12" md="6">
						<v-text-field
							v-model="filters.name"
							label="Search by name"
							density="comfortable"
							@input="fetchStudents"
							hide-details
						></v-text-field>
					</v-col>
					<v-col cols="12" md="6">
						<v-autocomplete
							v-model="filters.classroom"
							:items="classrooms"
							label="Filter by classroom"
							:item-props="getClassroomInfoFromObj"
							density="comfortable"
							clearable
							@update:model-value="fetchStudents"
							hide-details
						></v-autocomplete>
					</v-col>
				</v-row>
			</v-card-title>

			<v-data-table
				:headers="headers"
				:items="students"
				:loading="loading"
			>
				<template #item="{ item }">
					<tr>
						<td>{{ item.user.full_name }}</td>
						<td>{{ item.student_no }}</td>
						<td> 
							<v-checkbox
								v-model="item.user.is_approved"
							></v-checkbox>
						</td>
						<td>
							<v-checkbox
								v-model="item.user.is_active"
							></v-checkbox>
						</td>
					</tr>
				</template>
			</v-data-table>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { getStudents } from "@/apps/students/api";
import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";

const students = ref([]);
const classrooms = ref([]);
const loading = ref(false);

const filters = ref({
	name: "",
	classroom: null,
});

const headers = [
	{ title: "Name", key: "user.full_name" },
	{ title: "Student No", key: "student_no" },
	{ title: "Approved", key: "user.is_approved" },
	{ title: "Active", key: "user.is_active" },
	{ title: "", key: "actions", align: "end", sortable: false },
];

const fetchStudents = async () => {
	loading.value = true;
	try {
		const filter = {};
		if (filters.value.name) filter.name = filters.value.name;
		if (filters.value.classroom) filter.classroom = filters.value.classroom;

		students.value = (await getStudents(filter)).results;
	} catch (error) {
		console.error("Error fetching students:", error);
	} finally {
		loading.value = false;
	}
};

onMounted(async () => {
	classrooms.value = (await getClassrooms()).results;
});

watch(() => filters.value, fetchStudents, { deep: true });

// Initial fetch
fetchStudents();
</script>
