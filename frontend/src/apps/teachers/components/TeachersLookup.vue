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
import FilterCard from "@/components/FilterCard.vue";

const classrooms = ref([]);

const filters = ref({
	name: "",
	classrooms: null,
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
	{ title: "Name", key: "user_details", formatFunc: (ud) => ud.full_name },
	{ title: "Teacher Id", key: "identifier" },
	{ title: "", key: "actions", align: "end", sortable: false },
];

onMounted(async () => {
	classrooms.value = (await getClassrooms()).results;
});
</script>
