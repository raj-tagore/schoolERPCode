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
						:action="handleCreateAttachment.bind({isActive})"
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
import { ref, computed } from "vue";
import FormCard from "@/components/FormCard.vue";
import { createAttachment } from "@/apps/attachments/api";

const props = defineProps({
	getButtonText: {
		type: Function,
		default: () => "Add Attachment",
	},
	title: {
		type: String,
		default: "Add Attachment",
	},
	modelValue: {
		type: Array,
		required: true,
	},
});

const attachment = ref(null);

const buttonText = computed(() => {
	const newButtonText = props.getButtonText(attachment.value);
	return newButtonText ? newButtonText : "Add Attachment";
});

const emit = defineEmits("update:modelValue");

async function handleCreateAttachment(data) {
	try {
		attachment.value = await createAttachment(data);
		emit("update:modelValue", attachment?.value?.map((a) => a.id));
		this.isActive.value = false;
		return { success: true };
	} catch (error) {
		console.error(`Failed to ${props.actionName} ${props.title}:`, error);
		return { success: false, error };
	}
}

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

