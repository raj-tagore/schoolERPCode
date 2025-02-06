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
				</v-row>
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


const filters = ref({
	name: "",
});

const headers = [
	{ title: "Name", key: "user_details", formatFunc: (ud) => ud.full_name },
	{ title: "", key: "actions", align: "end", sortable: false },
];

</script>
