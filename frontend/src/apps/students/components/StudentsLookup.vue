<template>
	<v-container>
		<v-card variant="flat">
			<v-card-title>
				<FilterCard 
					v-model="filters"
					:filtersInfo="filtersInfo" 
				/>
			</v-card-title>

			<ResponsiveDataTable 
				:getToFunction="(item) => ({ name: 'Student', params: { studentId: item.id }})" 
				:headers="headers" 
				:fetch="getStudents" 
				v-model="filters"
				:forceMobile="forceMobile"
			/>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref } from "vue";
import { getStudents } from "@/apps/students/api";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import FilterCard from "@/components/FilterCard.vue";

const filters = ref({
	name: "",
	classroom: null,
});

const filtersInfo = ref([
	{
		label: "Search by name",
		type: "string",
		key: "name",
	},
	{
		label: "Filter by classroom",
		type: "classroom",
		key: "classrooms",
	},
]);

const headers = [
	{ title: "Name", key: "user_details", formatFunc: (item) => item.full_name },
	{ title: "Student No", key: "student_no" },
	{ title: "", key: "actions", align: "end", sortable: false },
];
</script>
