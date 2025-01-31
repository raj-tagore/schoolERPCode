<template>
	<v-container>
		<FormCard 
			title="Student Settings"
			:onSubmit="handleUpdate">
			<v-row v-if="user">
				<v-col>
					<v-text-field 
						label="First Name" 
						v-model="user.first_name"
						:rules="[v => !!v || 'First Name is required']"
						required
					></v-text-field>
					<v-text-field 
						label="Last Name" 
						v-model="user.last_name"
						:rules="[v => !!v || 'Last Name is required']"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row v-if="user">
				<v-col>
					<v-text-field 
						label="E-Mail" 
						v-model="user.email"
						:rules="[v => !!v || 'E-Mail is required']"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row v-if="user">
				<v-col>
					<v-checkbox 
						label="Is Active" 
						v-model="user.is_active"
					></v-checkbox>
				</v-col>
				<v-col>
					<v-checkbox 
						label="Is Approved" 
						v-model="user.is_approved"
					></v-checkbox>
				</v-col>
			</v-row>
		</FormCard>
	</v-container>
</template>

<script setup>
import { ref } from "vue";
import FormCard from "@/components/FormCard.vue";
import { updateStudent, updateUser } from "@/apps/users/api";

const props = defineProps({
	student: {
		type: Object,
		required: true
	},
	user: {
		type: Object,
		required: true
	}
});

const handleUpdate = async () => {
	try {
		await updateStudent(props.student);
		await updateUser(props.user);
		return { success: true };
	} catch (error) {
		console.error("Failed to update student:", error);
		return { success: false, error };
	}
};
</script>
