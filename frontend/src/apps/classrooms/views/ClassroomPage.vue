<template>
	<v-container>
	<v-row align="center" justify="center" v-if="classroom">
		<v-col>
			<v-card>
				<v-tabs
					background-color="deep-purple accent-4"
					center-active
					dark
					density="comfortable"
					align-tabs="center"
					v-model="tabs"
				>
					<v-tab>Student View</v-tab>
					<v-tab>Settings</v-tab>
					<v-tab>Members</v-tab>
				</v-tabs>
			</v-card>
			<v-tabs-window v-model="tabs">
				<v-tabs-window-item>
					<v-row class="ma-2">
						<v-col cols="12" lg="4">
							<ClassroomCard :classroomId="classroomId" />
						</v-col>
						<v-col cols="12" lg="4">
							<SubjectsCard :url="`api/allocation/subjects/all/?classroom=${classroom.id}`" />
						</v-col>
						<v-col cols="12" lg="4">
							<AnnouncementsCard :url="`api/announcements/all/?classroom=${classroom.id}`" />
						</v-col>
					</v-row>
				</v-tabs-window-item>
				<v-tabs-window-item>
					<ClassroomSettings :classroomId="classroomId" />
				</v-tabs-window-item>
				<v-tabs-window-item>
					<v-row>
						<v-col cols="12" lg="6">
							<TeachersTable :filter="{ classrooms: classroom.id }" />
						</v-col>
						<v-col cols="12" lg="6">
							<StudentsTable :filter="{ classrooms: classroom.id }" />
						</v-col>
					</v-row>
				</v-tabs-window-item>
			</v-tabs-window>
		</v-col>
	</v-row>
</v-container>
</template>

<script setup>
import {
	getClassroom,
} from "@/apps/classrooms/api";

import { ref } from "vue";

// biome-ignore lint/style/useConst: Biome does not support vue yet
let tabs = ref(null);
let classroom = ref(null);

const props = defineProps({
	classroomId: Number,
});

import AnnouncementsCard from "@/apps/announcements/components/AnnouncementsCard.vue";
import SubjectsCard from "@/apps/subjects/components/SubjectCards.vue";
import StudentsTable from "@/apps/users/components/StudentsTable.vue";
import TeachersTable from "@/apps/users/components/TeachersTable.vue";
import ClassroomCard from "@/apps/classrooms/components/ClassroomCard.vue"
import ClassroomSettings from "@/apps/classrooms/components/ClassroomSettings.vue"

classroom = await getClassroom(props.classroomId);
</script>
