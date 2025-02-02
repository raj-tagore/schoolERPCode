<template>
	<v-dialog>
		<template v-slot:activator="{ props:activatorProps }">
			<v-btn
				v-bind="activatorProps"
				rounded
				:text="buttonText"
				color="primary"
			/>
		</template>
		<template v-slot:default="{ isActive }">
			<v-card>
				<v-card-text>
					<FormCard
						:title="title"
						actionName="Create"
						:model="model"
						:action="handleCreateAttachment"
					/>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn
						text="Close"
						@click="isActive.value = false"
					></v-btn>
				</v-card-actions>
			</v-card>
		</template>
	</v-dialog>
</template>

<script setup>
import { ref } from "vue";
import FormCard from "@/components/FormCard.vue";
import { createAttachment } from "@/apps/attachments/api";

const props = defineProps({
	buttonText: {
		type: String,
		default: "Add Attachment",
	},
	title: {
		type: String,
		default: "Add Attachment",
	},
	onCreate: {
		type: Function,
		default: () => {},
	},
});

const handleCreateAttachment = async (data) => {
	try {
		const newAttachment = await createAttachment(data);
		await props.onCreate(newAttachment);
		return { success: true };
	} catch (error) {
		console.error(`Failed to ${props.actionName} ${props.title}:`, error);
		return { success: false, error };
	}
};

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

