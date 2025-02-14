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
			<v-number-input
				v-if="field.type === 'integer'"
				:label="field.label" 
				v-model="filters[field.key]"
				:rules="[v => !!v || `${field.label} is required`]"
				density="comfortable"
				hide-details
				:disabled="field.disabled"
			></v-number-input>
			<ServerAutocomplete
				v-if="['number', 'classroom', 'subject', 'teacher', 'student', 'payment_purpose'].includes(field.type)"
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
			<v-date-input
				v-if="field.type === 'dates'"
				color="primary"
				:label="field.label" 
				:multiple="field.key.length"
				density="comfortable"
				clearable
				:disabled="field.disabled"
				@update:modelValue="(value) => [...value].sort((a,b) => a - b).forEach((e, i) => {console.log(i, e);filters[field.key[i]] = e})"
			></v-date-input>
			<!--- The above one-liner does the following
			- Gets the dates in an array from datepicker
			- Sorts them, treating them as a number
			- Assigns the corresponding date to the corresponding field in filter
			--->
		</v-col>
	</v-row>
</template>

<script setup>
import { getClassroomInfoFromObj, getClassrooms } from "@/apps/classrooms/api";
import {
	getPayeeInfoFromObj,
	getPayees,
	getPaymentPurposeInfoFromObj,
	getPaymentPurposes,
} from "@/apps/finances/api";
import { getSubjectInfoFromObj, getSubjects } from "@/apps/subjects/api";
import { getTeacherInfoFromObj, getTeachers } from "@/apps/teachers/api";
import { getStudentInfoFromObj, getStudents } from "@/apps/students/api";

import ServerAutocomplete from "@/components/ServerAutocomplete.vue";

const props = defineProps({
	// Each element for this array will be an object with the following keys:
	// - label: String
	// - key: String & [String] for date range
	// - type: String
	//   - 'string'
	//   - 'integer'
	//   - 'number'
	//   - 'boolean'
	//   - 'array'
	//   - 'n_nary'
	//   - 'classroom'
	//   - 'subject'
	//   - 'teacher'
	//   - 'student'
	//   - 'payment_purpose'
	//   - 'dates'
	// - fetchOptions: Function? (only for custom number/array types)
	// - fetchOptionsInfo: Function? (only for custom number/array types)
	// - searchField: String? (defaults to 'name')
	filtersInfo: {
		type: Array,
		required: true,
	},
});

const filters = defineModel();

const getFilterFetch = (field) => {
	switch (field.type) {
		case "classroom":
			return getClassrooms;
		case "subject":
			return getSubjects;
		case "teacher":
			return getTeachers;
		case "payment_purpose":
			return getPaymentPurposes;
		case "payee":
			return getPayees;
		case "student":
			return getStudents;
		default:
			return field.fetchOptions;
	}
};

const getFilterInfo = (field) => {
	switch (field.type) {
		case "classroom":
			return getClassroomInfoFromObj;
		case "subject":
			return getSubjectInfoFromObj;
		case "teacher":
			return getTeacherInfoFromObj;
		case "payment_purpose":
			return getPaymentPurposeInfoFromObj;
		case "payee":
			return getPayeeInfoFromObj;
		case "student":
			return getStudentInfoFromObj;
		default:
			return field.fetchOptionsInfo;
	}
};
</script>
