<template>
	<v-container>
		<v-row align="center" justify="center">
			<v-col>
				<ClassroomSettings :classroomId="classroomId" />
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import ClassroomSettings from "@/apps/classrooms/components/ClassroomSettingsCard.vue";

const props = defineProps({
	classroomId: Number,
});
</script>
