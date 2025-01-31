<template>
	<v-container>
		<v-row align="center" justify="center">
			<v-col>
				<SubjectSettingsCard v-if="subject" :subject="subject"/>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getSubject } from "@/apps/subjects/api";
const props = defineProps({
	subjectId: String,
});
const subject = ref(null);

onMounted(async () => {
	subject.value = getSubject(props.subjectId);
});
</script>
