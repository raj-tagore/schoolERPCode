<template>
	<v-container>
	<v-row align="center" justify="center" v-if="this.classroom">
		<v-col>
			<v-card>
				<v-tabs
					background-color="deep-purple accent-4"
					center-active
					dark
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
									:src="getRandomClassroomImage()" 
									class="custom-img"
								></v-img>
								<v-card-title>
									{{this.classroom.name}}
									<p class="text-body-2 pb-4">
										<b>Standard: </b>{{this.classroom.standard}} <br>
										<b>Class Teacher: </b>{{ this.classroom.class_teacher_details?.user?.first_name || "Loading..." }}
									</p>
								</v-card-title>
							</v-card>
						</v-col>
						<v-col cols="12" lg="4">
							<v-card>
								<v-card-title>Subjects</v-card-title>
								<v-card-text>
									<v-row>
										<v-col v-for="subject in subjects" :key="subject.id" cols="6">
											<v-card>
												<v-card-title class="text-body-1">{{ subject.name }}</v-card-title>
												<v-card-subtitle v-if="subject.teacher_details">{{ subject.teacher_details.user.first_name + ' ' + subject.teacher_details.user.last_name }}</v-card-subtitle>
												<v-card-actions class="justify-center">
													<v-btn :to="{name: 'Subject', params: {subjectId: subject.id}}">Enter</v-btn>
												</v-card-actions>
											</v-card>
										</v-col>
									</v-row>
								</v-card-text>
							</v-card>
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
					<v-row class="ma-2">
						<v-col>
							<ClassroomTeacherTable :classroom="classroom">
							</ClassroomTeacherTable>
						</v-col>
						<v-col>
							<ClassroomStudentTable :classroom="classroom">
							</ClassroomStudentTable>
						</v-col>
					</v-row>
				</v-tabs-window-item>
			</v-tabs-window>
		</v-col>
	</v-row>
</v-container>
</template>

<script>
import api from "@/services/api";

import { getClassroom, getClassroomSubjects } from "@/services/api";

import ClassroomStudentTable from "@/components/ClassroomStudentTable.vue";
import ClassroomTeacherTable from "@/components/ClassroomTeacherTable.vue";
import AnnouncementCards from "@/components/AnnouncementCards.vue";

export default {
	components: {
		ClassroomTeacherTable,
		ClassroomStudentTable,
		AnnouncementCards,
	},
	data() {
		return {
			tabs: null,
			classroom: null,
			teachers: [],
			subjects: [],
			images: [
				require("@/assets/classrooms/classroom1.png"),
				require("@/assets/classrooms/classroom2.png"),
				require("@/assets/classrooms/classroom3.png"),
			],
		};
	},
	props: ["classroomId"],
	methods: {
		getRandomClassroomImage() {
			const index = Math.floor(Math.random() * this.images.length);
			return this.images[index];
		},
		async updateClassroom() {
			const classroom = structuredClone(this.classroom);
			classroom.class_teacher_details = null;
			await api.put(
				`api/allocation/classrooms/${this.classroomId}/`,
				classroom,
			);
		},

		async getTeachers() {
			this.teachers = (await api.get("api/accounts/teachers/all")).data;
		},

		teacherInfoFromObj(item) {
			return {
				title: `${item.user.first_name} ${item.user.last_name}`,
				subtitle: item.identifier,
				value: item.id,
			};
		},

		async getClassroomData() {
			this.classroom = await getClassroom(this.classroomId);
			this.subjects = await getClassroomSubjects(this.classroomId);
		},
	},
	mounted() {
		this.getClassroomData();
		this.getTeachers();
	},
};
</script>
