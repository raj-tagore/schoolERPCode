<template>
	<FormCard
		:title="title"
		actionName="Add"
		:model="model"
		:action="handleCreateAttachment"
		class="border mb-4"
		variant="flat"
	/>
</template>

<script setup>
import { ref } from "vue";
import FormCard from "@/components/FormCard.vue";
import { createAttachment } from "@/apps/attachments/api";

const props = defineProps({
	title: {
		type: String,
		default: "Attachment",
	},
	required: {
		type: Boolean,
	},
});

const attachment = ref(null);

const emit = defineEmits(["update:attachment"]);

async function handleCreateAttachment(data) {
	attachment.value = await createAttachment(data);
	emit("update:attachment", attachment?.value);
	attachment.value = null;  // Reset the attachment after emitting
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
		required: props.required,
	},
]);
</script>
