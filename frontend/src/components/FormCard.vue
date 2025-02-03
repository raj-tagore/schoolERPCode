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
						:required="field.required"
					></v-text-field>
					<v-textarea 
						v-if="field.type === 'longstring'"
						:label="field.label" 
						v-model="newValue[field.key]"
						:rules="[v => !!v || `${field.label} is required`]"
						:required="field.required"
					></v-textarea>
					<v-select
						v-if="field.type === 'select'"
						:label="field.label"
						v-model="newValue[field.key]"
						:items="field.items"
						:required="field.required"
					></v-select>
					<v-text-field
						v-if="field.type === 'datetime'"
						:label="field.label"
						type="datetime-local"
						v-model="newValue[field.key]"
						:rules="[v => !!v || `${field.label} is required`]"
						:required="field.required"
					></v-text-field>
					<ServerAutocomplete
						v-if="field.type === 'number'"
						v-model="newValue[field.key]"
						:fetch="field.fetchOptions"
						:getInfo="field.fetchOptionsInfo"
						:searchField="field.searchField"
						:label="field.label"
						:required="field.required"
					/>
					<v-checkbox 
						v-if="field.type === 'boolean'"
						:label="field.label" 
						v-model="newValue[field.key]"
						:required="field.required"
					></v-checkbox>
					<ServerAutocomplete
						v-if="field.type === 'array'"
						v-model="newValue[field.key]"
						:fetch="field.fetchOptions"
						:getInfo="field.fetchOptionsInfo"
						:searchField="field.searchField"
						:label="field.label"
						:multiple='true'
						:required="field.required"
					/>
					<v-file-input
						v-if="field.type === 'file'"
						v-model="newValue[field.key]"
						:label="field.label"
						:required="field.required"
						show-size
						counter
					></v-file-input>
					<AttachmentForm
						v-if="field.type === 'attachment'"
						@update:attachments="(v) => newValue[field.key] = v"
						:required="field.required"
						show-size
					/>
					<AttachmentsForm
						v-if="field.type === 'attachment_list'"
						@update:attachment="(v) => newValue[field.key] = v"
						:required="field.required"
						show-size
					/>
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
import { ref } from "vue";
import SubmitButton from "@/components/SubmitButton.vue";
import ServerAutocomplete from "@/components/ServerAutocomplete.vue";
import AttachmentForm from "@/apps/attachments/components/AttachmentForm.vue";
import AttachmentsForm from "@/apps/attachments/components/AttachmentsForm.vue";

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
	//   - 'attachment'
	//   - 'attachment_list'
	// - fetchOptions: Function?
	// - fetchOptionsInfo: Function?
	// - searchField: String?
	// - defaultValue: Any
	// - required
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
