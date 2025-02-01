<template>
	<v-container>
		<v-card>
			<v-card-title>
				Create New Classroom
			</v-card-title>
			<v-card-text>
				<v-row>
					<v-col cols="12" lg="6" v-for="field in model">
						<v-text-field 
							label="Name" 
							v-model="classroom.name"
							:rules="[v => !!v || 'Name is required']"
							required
						></v-text-field>
					</v-col>
					<v-col>
						<v-text-field 
							label="Standard" 
							v-model="classroom.standard"
							type="number"
							:rules="[v => !!v || 'Standard is required']"
							required
						></v-text-field>
						<v-text-field 
							label="Name" 
							v-model="classroom.name"
							:rules="[v => !!v || 'Name is required']"
							required
						></v-text-field>
					</v-col>
				</v-row>
				<v-row>
					<v-col>
						<ServerAutocomplete
							v-model="classroom.class_teacher"
							:fetch="getTeachers"
							:getInfo="getTeacherInfoFromObj"
							searchField="name"
							label="Class Teacher"
						/>
					</v-col>
					<v-col>
						<v-checkbox 
							label="Is Active" 
							v-model="classroom.is_active"
						></v-checkbox>
					</v-col>
				</v-row>
				<v-row>
					<v-col>
						<ServerAutocomplete
							v-model="classroom.other_teachers"
							:fetch="getTeachers"
							:getInfo="getTeacherInfoFromObj"
							searchField="name"
							label="Other Teachers"
							:multiple="true"
						/>
					</v-col>
				</v-row>
				<v-row>
					<v-col>
						<ServerAutocomplete
							v-model="classroom.students"
							:fetch="getStudents"
							:getInfo="getStudentInfoFromObj"
							searchField="name"
							label="Students"
							:multiple="true"
						/>
					</v-col>
				</v-row>
				<SubmitButton 
					:onSubmit="handleCreate"
					submitText="Create"
				/>
			</v-card-text>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref } from "vue";
import { createClassroom } from "@/apps/classrooms/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/teachers/api";
import { getStudents, getStudentInfoFromObj } from "@/apps/students/api";
import SubmitButton from "@/components/SubmitButton.vue";
import ServerAutocomplete from "@/components/ServerAutocomplete.vue";

const props = defineProps({
	title: {
		type: String,
		required: true,
	},
	// Each element for this array will be an object with the following keys:
	// - label: String
	// - key: String
	// - defaultValue: Any
	// - fetchOptions: Function?
	model: {
		type: Array,
		required: true,
	},
	create: {
		type: Function,
		required: true,
	},
});

const value = ref(
	props.model.reduce((acc, { key, defaultValue }) => {
		acc[key] = defaultValue;
		return acc;
	}, {}),
);

const classroom = ref({
	name: "",
	standard: null,
	is_active: true,
	class_teacher: null,
	students: [],
	other_teachers: [],
});

const handleCreate = async () => {
	try {
		await createClassroom(classroom.value);
		return { success: true };
	} catch (error) {
		console.error("Failed to create classroom:", error);
		return { success: false, error };
	}
};
</script>
