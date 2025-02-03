<template>
	<AttachmentForm :required="required" :title="title" @update:attachment="attachmentAdded" />
	<v-col v-for="item in attachments">
		<v-card :title="item.name">
			<v-card-text>
				<v-col>
					{{item.file.name}}
				</v-col>
				<v-col>
					<v-btn @click="removeAttachment(item)">
						<v-icon>mdi-close</v-icon>
					</v-btn>
				</v-col>
			</v-card-text>
		</v-card>
	</v-col>
</template>

<script setup>
import AttachmentForm from "@/apps/attachments/components/AttachmentForm.vue";
import { ref } from "vue";

const attachments = ref([]);

const props = defineProps({
	title: {
		type: String,
		default: "Attachments",
	},
	required: {
		type: Boolean,
	},
});

const emit = defineEmits(["update:attachments"]);

const attachmentAdded = (item) => {
	attachments.value.push(item);
	emit("update:attachments", attachments.value);
};

const removeAttachment = (item) => {
	const idx = attachments.value.map((a) => a.id).indexOf(item.id);
	if (idx < 0) {
		console.error("Attachment idx when removing from attachments is negative");
		console.error("This should never happen");
		return;
	}
	attachments.value.splice(idx, 1);
};
</script>
