<template>
	<v-container>
		<v-row align="center" justify="center" v-if="classroom">
			<v-col>
				<v-row class="ma-2">
					<v-col cols="12" lg="4">
						<ClassroomCard :classroomId="classroomId" />
					</v-col>
					<v-col cols="12" lg="4">
						<SubjectsList :filter="{ classroom: classroom.id }" />
					</v-col>
					<v-col cols="12" lg="4">
						<AnnouncementsList :filter="{ classroom: classroom.id }" />
					</v-col>
				</v-row>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import { getClassroom } from "@/apps/classrooms/api";
import { ref } from "vue";

const classroom = ref(null);

const props = defineProps({
	classroomId: Number,
});

import AnnouncementsList from "@/apps/announcements/components/AnnouncementsList.vue";
import SubjectsList from "@/apps/subjects/components/SubjectsList.vue";
import ClassroomCard from "@/apps/classrooms/components/ClassroomCard.vue";
import AnnouncementsLookup from "@/apps/announcements/components/AnnouncementsLookup.vue";
import AssignmentsLookup from "@/apps/assignments/components/AssignmentsLookup.vue";

classroom.value = await getClassroom(props.classroomId);
</script>
