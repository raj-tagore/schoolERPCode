<template>
	<v-card>
		<v-card-title>
			{{actionName}} {{ title }}
		</v-card-title>
		<v-card-text>
			<v-row>
				<v-col cols="12" :lg="field.type === 'longstring' ? 12 : 6" v-for="field in model">
					<v-text-field 
						v-if="field.type === 'string'"
						:label="field.label" 
						v-model="newValue[field.key]"
						:rules="[v => !!v || `${field.label} is required`]"
						required
					></v-text-field>
					<v-textarea 
						v-if="field.type === 'longstring'"
						:label="field.label" 
						v-model="newValue[field.key]"
						:rules="[v => !!v || `${field.label} is required`]"
						required
					></v-textarea>
					<v-select
						v-if="field.type === 'select'"
						:label="field.label"
						v-model="newValue[field.key]"
						:items="field.items"
					></v-select>
					<v-text-field
						v-if="field.type === 'datetime'"
						:label="field.label"
						type="datetime-local"
						v-model="newValue[field.key]"
						:rules="[v => !!v || `${field.label} is required`]"
						required
					></v-text-field>
					<ServerAutocomplete
						v-if="field.type === 'number'"
						v-model="newValue[field.key]"
						:fetch="field.fetchOptions"
						:getInfo="field.fetchOptionsInfo"
						:searchField="field.searchField"
						:label="field.label"
					/>
					<v-checkbox 
						v-if="field.type === 'boolean'"
						:label="field.label" 
						v-model="newValue[field.key]"
					></v-checkbox>
					<ServerAutocomplete
						v-if="field.type === 'array'"
						v-model="newValue[field.key]"
						:fetch="field.fetchOptions"
						:getInfo="field.fetchOptionsInfo"
						:searchField="field.searchField"
						:label="field.label"
						:multiple='true'
					/>
					<v-file-input
						v-if="field.type === 'file'"
						v-model="newValue[field.key]"
						:label="field.label"
						required
						show-size
					></v-file-input>
				</v-col>
			</v-row>
			<SubmitButton 
				:onSubmit="handleAction"
				:submitText="actionName"
			/>
		</v-card-text>
	</v-card>
</template>

<script setup>
import { ref, watch } from "vue";
import SubmitButton from "@/components/SubmitButton.vue";
import ServerAutocomplete from "@/components/ServerAutocomplete.vue";

const props = defineProps({
	title: {
		type: String,
		required: true,
	},
	actionName: {
		type: String,
		required: true,
	},
	// Each element for this array will be an object with the following keys:
	// - label: String
	// - key: String
	// - type: String
	//   - 'string'
	//   - 'number'
	//   - 'boolean'
	//	 - 'array'
	//   - 'longstring'
	//   - 'file'
	// - fetchOptions: Function?
	// - fetchOptionsInfo: Function?
	// - searchField: String?
	// - defaultValue: Any
	model: {
		type: Array,
		required: true,
	},
	action: {
		type: Function,
		required: true,
	},
});

const newValue = ref(
	props.model.reduce((acc, { key, defaultValue }) => {
		acc[key] = defaultValue;
		return acc;
	}, {}),
);

const handleAction = async () => {
	try {
		await props.action(newValue.value);
		return { success: true };
	} catch (error) {
		console.error(`Failed to ${props.actionName} ${props.title}:`, error);
		return { success: false, error };
	}
};
</script>
