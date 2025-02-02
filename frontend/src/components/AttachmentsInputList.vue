<template>
	<v-row v-for="item in attachments">
		<v-card :title="item.name">
			<v-card-text>
				<v-row>
					<v-col>
						{{item.file.name}}
					</v-col>
					<v-col>
						<v-btn @click="removeAttachment(item)">
							<v-icon>mdi-close</v-icon>
						</v-btn>
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

const removeAttachment = (item) => {
	const idx = attachments.value.map((a) => a.id).indexOf(item.id);
	if (idx < 0) {
		console.error("Attachment idx when removing from attachments is negative")
		console.error("This should never happen")
		return
	}
	attachments.value.splice(idx, 1)
}

watch(attachment, (newAttachment) => {
	if (newAttachment) {
		attachments.value.push(newAttachment);
		attachment.value = null;
	}
});

watch(attachments.value, (attachments) => {
	emit(
		"update:modelValue",
		attachments.map((a) => a.id),
	);
	emit("update:attachmentItems", attachments);
});
</script>
