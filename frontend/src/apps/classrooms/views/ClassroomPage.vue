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
							<v-card>
								<v-img 
									:src="getClassroomImage()" 
									class="custom-img"
								></v-img>
								<v-card-title>
									{{classroom.name}}
								</v-card-title>
								<v-card-subtitle>
									<p class="text-body-2 pb-4">
										Standard: {{classroom.standard}} <br>
										Class Teacher: {{ classroom.class_teacher_details?.user?.first_name || "Loading..." }}
									</p>
								</v-card-subtitle>
							</v-card>
						</v-col>
						<v-col cols="12" lg="4">
							<SubjectCards :url="`api/allocation/subjects/all/?classroom=${classroom.id}`" />
						</v-col>
						<v-col cols="12" lg="4">
							<AnnouncementCards :url="`api/announcements/all/?classroom=${classroom.id}`" />
						</v-col>
					</v-row>
				</v-tabs-window-item>
				<v-tabs-window-item>
					<v-card class="ma-4 pa-4">
						<v-card-title>Settings</v-card-title>
						<v-card-text>
							<v-row>
								<v-col cols="12" lg="6">
									<v-text-field label="Standard" v-model="classroom.standard"></v-text-field>
								</v-col>
								<v-col cols="12" lg="6">
									<v-text-field label="Name" v-model="classroom.name"></v-text-field>
								</v-col>
							</v-row>
							<v-row>
								<v-col cols="12" lg="6">
									<v-autocomplete label="Class Teacher" :item-props="teacherInfoFromObj" :items="teachers" v-model="classroom.class_teacher"></v-autocomplete>
								</v-col>
								<v-col cols="12" lg="6">
									<v-checkbox label="Is Active" v-model="classroom.is_active"></v-checkbox>
								</v-col>
							</v-row>
							<v-row>
								<v-btn @click="updateClassroom()" color="primary">Update</v-btn>
							</v-row>
						</v-card-text>
					</v-card>
				</v-tabs-window-item>
				<v-tabs-window-item>
					Lead Teacher
					<TeacherTable :filter="{ classrooms_leading: classroom.id }" />
					Assisting Teachers
					<TeacherTable :filter="{ classrooms_assisting: classroom.id }" />
					<StudentTable :filter="{ classroom: classroom.id }" />
				</v-tabs-window-item>
			</v-tabs-window>
		</v-col>
	</v-row>
</v-container>
</template>

<script setup>
import {
	getClassroom,
	getClassroomImage,
} from "@/apps/classrooms/api";

import { ref } from "vue";

// biome-ignore lint/style/useConst: Biome does not support vue yet
let tabs = ref(null);
let classroom = ref(null);

const props = defineProps({
	classroomId: Number,
});

import AnnouncementCards from "@/apps/announcements/components/AnnouncementsCard.vue";
import SubjectCards from "@/apps/subjects/components/SubjectCards.vue";
import StudentTable from "@/apps/users/components/StudentTable.vue";
import TeacherTable from "@/apps/users/components/TeacherTable.vue";

classroom = await getClassroom(props.classroomId);


</script>
