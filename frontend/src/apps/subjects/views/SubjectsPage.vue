<template>
	<v-container>
	<v-row>
		<v-col md="4">
			<v-text-field
				v-model="search"
				label="Search for your classroom"
				density="comfortable"
				@update:model-value="updateFilter"
				clearable
			/>
		</v-col>
	</v-row>
	<SubjectsCard :filter="filter" />
	</v-container>
</template>

<script setup>
import SubjectsCard from "@/apps/subjects/components/SubjectsCard.vue";
import { reactive, ref } from "vue";

const search = ref("");
const filter = reactive({});

const updateFilter = (value) => {
	if (value) {
		filter.name = value;
	} else {
		delete filter.name;
	}
};
</script>
