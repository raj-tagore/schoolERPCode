<template>
	<v-row>
		<v-col cols="12" lg="6">
			<AttachmentForm :required="required" :title="title" @update:attachment="attachmentAdded" />
		</v-col>
		<v-col cols="12" lg="6">
			<v-list density="compact" class="mt-2" v-if="attachments.length > 0">
				Added Attachments:
				<v-list-item
					v-for="item in attachments"
					:key="item.id"
					:title="item.name"
					:subtitle="item.file.name"
					variant="outlined"
					class="mb-2"
				>
					<template v-slot:append>
						<v-btn 
							icon="mdi-close" 
							size="small" 
							variant="text" 
							density="compact"
							@click="removeAttachment(item)"
						></v-btn>
					</template>
				</v-list-item>
			</v-list>
		</v-col>
	</v-row>
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
