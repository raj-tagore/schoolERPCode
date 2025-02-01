<template>
	<v-container>
		<v-row>
			<v-col>
				<AssignmentSettings :assignmentId="assignmentId"></AssignmentSettings>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>

import AssignmentSettings from "@/apps/assignments/components/AssignmentSettings.vue";

const props = defineProps({
	assignmentId: Number,
});

</script>
