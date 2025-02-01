<template>
	<v-row>
		<v-col cols="12" md="4" lg="3" v-for="field in filtersInfo">
			<v-text-field 
				v-if="field.type === 'string'"
				:label="field.label" 
				v-model="filters[field.key]"
				:rules="[v => !!v || `${field.label} is required`]"
				density="comfortable"
				hide-details
			></v-text-field>
			<ServerAutocomplete
				v-if="field.type === 'number'"
				v-model="filters[field.key]"
				clearable
				:fetch="field.fetchOptions"
				:getInfo="field.fetchOptionsInfo"
				:searchField="field.searchField"
				:label="field.label"
			/>
			<v-checkbox 
				v-if="field.type === 'boolean'"
				:label="field.label" 
				v-model="filters[field.key]"
			></v-checkbox>
			<ServerAutocomplete
				v-if="field.type === 'array'"
				v-model="filters[field.key]"
				clearable
				:fetch="field.fetchOptions"
				:getInfo="field.fetchOptionsInfo"
				:searchField="field.searchField"
				:label="field.label"
				:multiple='true'
			/>
			<v-select
				v-if="field.type === 'n_nary'"
				v-model="filters[field.key]"
				:items="field.fetchOptions()"
				:label="field.label"
				hide-details
				density="comfortable"
			></v-select>
		</v-col>
	</v-row>
</template>

<script setup>
import { ref, watch } from "vue";
import ServerAutocomplete from "@/components/ServerAutocomplete.vue";

const props = defineProps({
	// Each element for this array will be an object with the following keys:
	// - label: String
	// - key: String
	// - type: String
	//   - 'string'
	//   - 'number'
	//   - 'boolean'
	//	 - 'array'
	//	 - 'n_nary'
	// - fetchOptions: Function?
	// - fetchOptionsInfo: Function?
	// - searchField: String?
	filtersInfo: {
		type: Array,
		required: true,
	},
	// The object that will be updated with the filters
	// The initial values are overwritten by the defaultValues
	defaultValues: {
		type: Object,
		default: () => ({}),
	},
	onFilterChange: {
		type: Function,
		required: true,
	},
});

const filters = ref(props.defaultValues);

const emit = defineEmits(["update:filters"]);

watch(filters.value, (newValue) => {
	emit("update:filters", structuredClone(newValue));
});
</script>
