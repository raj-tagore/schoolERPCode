<template>
	<v-row v-for="item in attachments">
		<v-card :title="item.name">
			<v-card-text>
				<v-row>
					<v-col>
						{{item.file.name}}
					</v-col>
				</v-row>
			</v-card-text>
		</v-card>
	</v-row>
	<v-row>
		<AttachmentInputButton :title="title" :getButtonText="getButtonText" v-model:attachment="attachment"  />
	</v-row>
</template>

<script setup>
import AttachmentInputButton from "@/components/AttachmentInputButton.vue";
import { ref, watch } from "vue";

const attachments = ref([]);

const attachment = ref({});

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
	attachmentItems: {
		type: Array,
	},
});

const emit = defineEmits(["update:modelValue", "update:attachmentItems"]);

watch(attachment, (newAttachment) => {
	console.log(newAttachment);
	if (newAttachment) {
		attachments.value.push(newAttachment);
		attachment.value = null;
	}
});

watch(attachments.value, (attachments) => {
	console.log(attachments);
	emit(
		"update:modelValue",
		attachments.map((a) => a.id),
	);
	emit("update:attachmentItems", attachments);
});
</script>
