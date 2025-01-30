<template>
	<v-container>
		<v-card>
			<v-card-title>
				Assignment Settings
			</v-card-title>
			<v-card-text>

				<v-row v-if="assignment">
					<v-col>
						<v-text-field 
							label="Title" 
							v-model="assignment.title"
							:rules="[v => !!v || 'Title is required']"
							required
						></v-text-field>
					</v-col>
					<v-col>
						<ServerAutocomplete
							:getInfo="getSubjectInfoFromObj"
							v-model="assignment.subject"
							:fetch="getSubjects"
							searchField="name"
							label="Subject"
						/>
					</v-col>
				</v-row>
				<v-row v-if="assignment">
					<v-col>
						<v-textarea 
							label="Description" 
							v-model="assignment.description"
							:rules="[v => !!v || 'Description is required']"
							required
						></v-textarea>
					</v-col>
				</v-row>
				<v-row v-if="assignment">
					<v-col>
						<v-text-field
							label="Release Date"
							type="datetime-local"
							v-model="assignment.release_at"
							:value="formatDateForInput(assignment.release_at)"
							@input="assignment.release_at = $event.target.value"
							:rules="[v => !!v || 'Release date is required']"
							required
						></v-text-field>
					</v-col>
					<v-col>
						<v-text-field
							label="Expiry Date"
							type="datetime-local"
							v-model="assignment.expiry_at"
							:value="formatDateForInput(assignment.expiry_at)"
							@input="assignment.expiry_at = $event.target.value"
							:rules="[v => !!v || 'Expiry date is required']"
							required
						></v-text-field>
					</v-col>
				</v-row>
				<v-row>
					<v-col>
						<v-checkbox 
							label="Is Active" 
							v-model="assignment.is_active"
						></v-checkbox>
					</v-col>
				</v-row>
				<SubmitButton 
					:onSubmit="handleUpdate"
				/>
			</v-card-text>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { getSubjects, getSubjectInfoFromObj } from "@/apps/subjects/api";
import { getAssignment, updateAssignment } from "@/apps/assignments/api";
import ServerAutocomplete from "@/components/ServerAutocomplete.vue";

import SubmitButton from "@/components/SubmitButton.vue";

const props = defineProps({
	assignmentId: {
		type: Number,
		required: true,
	},
});

const assignment = ref({});

watch(assignment, () => {
	console.log(assignment.value);
});

const handleUpdate = async () => await updateAssignment(assignment.value);

onMounted(async () => {
	assignment.value = await getAssignment(props.assignmentId);
});

const formatDateForInput = (dateString) => {
	if (!dateString) return "";
	return new Date(dateString).toISOString().slice(0, 16);
};
</script>

