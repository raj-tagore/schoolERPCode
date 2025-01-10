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
					density="comfortable"
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
						<ClassroomTeacherTable :classroom="classroom" @addTeacher="addTeacher" @removeTeacher="removeTeacher">
							</ClassroomTeacherTable>
						<ClassroomStudentTable :classroom="classroom" @addStudent="addStudent" @removeStudent="removeStudent">
							</ClassroomStudentTable>
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
import SubjectCards from "@/components/SubjectCards.vue";

export default {
	components: {
		ClassroomTeacherTable,
		ClassroomStudentTable,
		AnnouncementCards,
		SubjectCards,
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
			classroom.class_teacher_details = undefined;
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

		addTeacher(teacher) {
			this.classroom.other_teachers.push(teacher);
			this.updateClassroom();
		},

		removeTeacher(teacherId) {
			this.classroom.other_teachers.splice(
				this.classroom.other_teachers.indexOf(teacherId),
				1,
			);
			this.updateClassroom();
		},

		addStudent(student) {
			this.classroom.students.push(student);
			this.updateClassroom();
		},

		removeStudent(studentId) {
			this.classroom.students.splice(
				this.classroom.students.indexOf(studentId),
				1,
			);
			this.updateClassroom();
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
