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
				:disabled="field.disabled"
			></v-text-field>
			<ServerAutocomplete
				v-if="['number', 'classroom', 'subject', 'teacher'].includes(field.type)"
				v-model="filters[field.key]"
				:clearable="!field.disabled"
				:fetch="getFilterFetch(field)"
				:getInfo="getFilterInfo(field)"
				:searchField="field.searchField || 'name'"
				:label="field.label"
				density="comfortable"
				:disabled="field.disabled"
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
				:fetch="getFilterFetch(field)"
				:getInfo="getFilterInfo(field)"
				:searchField="field.searchField || 'name'"
				:label="field.label"
				:multiple='true'
				density="comfortable"
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
import ServerAutocomplete from "@/components/ServerAutocomplete.vue";
import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import { getSubjects, getSubjectInfoFromObj } from "@/apps/subjects/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";

const props = defineProps({
	// Each element for this array will be an object with the following keys:
	// - label: String
	// - key: String
	// - type: String
	//   - 'string'
	//   - 'number'
	//   - 'boolean'
	//   - 'array'
	//   - 'n_nary'
	//   - 'classroom'  // New type
	//   - 'subject'    // New type
	//   - 'teacher'    // New type
	// - fetchOptions: Function? (only for custom number/array types)
	// - fetchOptionsInfo: Function? (only for custom number/array types)
	// - searchField: String? (defaults to 'name')
	filtersInfo: {
		type: Array,
		required: true,
	},
});

const filters = defineModel({
	default: {},
});

const getFilterFetch = (field) => {
	switch (field.type) {
		case 'classroom':
			return getClassrooms;
		case 'subject':
			return getSubjects;
		case 'teacher':
			return getTeachers;
		default:
			return field.fetchOptions;
	}
};

const getFilterInfo = (field) => {
	switch (field.type) {
		case 'classroom':
			return getClassroomInfoFromObj;
		case 'subject':
			return getSubjectInfoFromObj;
		case 'teacher':
			return getTeacherInfoFromObj;
		default:
			return field.fetchOptionsInfo;
	}
};
</script>
