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
				:fetch="getParents"
				v-model="filters"
				:getToFunction="(item) => ({name: 'Parent', params: {parentId: item.id}})"
			/>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref } from "vue";
import { getParents } from "@/apps/parents/api";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import FilterCard from "@/components/FilterCard.vue";

const filters = ref({
	name: "",
});

const filtersInfo = ref([
	{
		label: "Search by name",
		type: "string",
		key: "name",
	},
]);

const headers = [
	{ title: "Name", key: "user_details", formatFunc: (ud) => ud.full_name },
	{ title: "", key: "actions", align: "end", sortable: false },
];

</script>
