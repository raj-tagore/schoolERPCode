<template>
	<v-container>
		<FormCard
			title="Attachment"
			actionName="Create"
			:model="model"
			:action="createAttachment"
		/>
	</v-container>
</template>

<script setup>
import { ref } from 'vue'
import FormCard from '@/components/FormCard.vue'
import { createAttachment } from '@/apps/attachments/api'

const model = ref([
	{
		label: "Name",
		key: "name",
		type: "string",
	},
	{
		label: "File",
		key: "file",
		type: "file",
	},
	{
		label: "Description",
		key: "description",
		type: "longstring",
	},
	{
		label: "Is Active",
		key: "is_active",
		type: "boolean",
	},
]);

</script>

