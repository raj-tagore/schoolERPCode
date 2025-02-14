<template>
	<v-btn 
		@click="handleSubmit" 
		color="primary"
		:loading="isSubmitting"
		:disabled="isSubmitting"
		:append-icon="isSuccess ? 'mdi-check' : (error ? 'mdi-alert' : '')"
		:color="error ? 'error' : 'primary'"
	>
		{{ isSuccess ? 'Updated!' : (error ? 'Failed!' : submitText) }}
	</v-btn>
	<v-alert
		v-if="error"
		type="error"
		class="mt-2"
		density="compact"
	>
		{{ error }}
	</v-alert>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
	submitText: {
		type: String,
		default: "Update",
	},
	onSubmit: {
		type: Function,
		required: true,
	},
});

const isSubmitting = ref(false);
const isSuccess = ref(false);
const error = ref(null);

const formatErrorMessage = (error) => {
	if (error.response) {
		const { status, data } = error.response;
		// Handle 400 Bad Request
		if (status === 400) {
			if (typeof data === "object") {
				// Format field-specific errors
				const errors = objToString(data);
				return errors;
			}
			return data.detail || "Invalid data submitted";
		}
		// Handle other status codes
		return data.detail || `Server returned ${status}`;
	}
	return "Failed to submit form";
};

const objToString = (data) => {
	if (Array.isArray(data)) {
		return data.join(", ");
	}
	if (typeof data === "string") {
		return data;
	}
	if (typeof data === "object") {
		return Object.entries(data).map(
			([field, message]) => `${field}: ${objToString(message)}`,
		);
	}
	return data;
};

const handleSubmit = async () => {
	isSubmitting.value = true;
	isSuccess.value = false;
	error.value = null;

	try {
		const result = await props.onSubmit();
		if (result.success) {
			isSuccess.value = true;
		} else {
			error.value = formatErrorMessage(result.error);
		}
		isSubmitting.value = false;
	} catch (err) {
		error.value = formatErrorMessage({ success: false, err });
	}
};
</script>
