<template>
	<v-container>
		<v-card variant="flat">
			<v-card-title>
				<v-row>
					<v-col cols="12" md="6">
						<v-text-field
							v-model="filters.name"
							label="Search by name"
							density="compact"
							hide-details
						></v-text-field>
					</v-col>
					<v-col cols="12" md="6">
						<v-autocomplete
							v-model="filters.classrooms"
							:items="classrooms"
							label="Filter by classroom"
							:item-props="getClassroomInfoFromObj"
							density="compact"
							clearable
							hide-details
						></v-autocomplete>
					</v-col>
				</v-row>
			</v-card-title>
			<ResponsiveDataTable
				:headers="headers"
				:fetch="getTeachers"
				v-model="filters"
				:getToFunction="(item) => ({name: 'Teacher', params: {teacherId: item.id}})"
			/>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getTeachers } from "@/apps/teachers/api";
import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";

const classrooms = ref([]);

const filters = ref({
	name: "",
	classrooms: null,
});

const headers = [
	{ title: "Name", key: "user_details", formatFunc: (ud) => ud.full_name },
	{ title: "Teacher Id", key: "identifier" },
	{ title: "", key: "actions", align: "end", sortable: false },
];

onMounted(async () => {
	classrooms.value = (await getClassrooms()).results;
});
</script>
