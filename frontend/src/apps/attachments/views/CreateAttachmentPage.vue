<template>
	<v-container>
		<FormCard
			title="Attachment"
			actionName="Create"
			:model="model"
			:action="() => {}"
		/>
	</v-container>
</template>

<script setup>
import { ref } from 'vue'
import FormCard from '@/components/FormCard.vue'

const model = ref([
	{
		label: "Attachment",
		key: "is_active",
		type: "attachment",
	},
]);

</script>

