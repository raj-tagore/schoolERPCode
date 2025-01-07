<template>
	<v-container v-if="this.classroom">
		<v-row align="center" justify="center">
			<v-col cols="12" lg="4">
				<v-card>
					<v-tabs
						background-color="deep-purple accent-4"
						center-active
						dark
						align-tabs="center"
						v-model="tabs"
					>
						<v-tab>Info</v-tab>
						<v-tab>Settings</v-tab>
					</v-tabs>
				</v-card>
				<v-tabs-window v-model="tabs">
					<v-tabs-window-item>
						<v-card>
							<v-img 
								:src="getRandomClassroomImage()" 
								class="custom-img"
							></v-img>
							<v-card-title class="text-body-1">{{this.classroom.standard}} - {{this.classroom.name}}</v-card-title>
							<v-card-subtitle>{{ this.classroom.class_teacher_details?.user?.first_name || "Loading..." }}</v-card-subtitle>
							<v-card-text>
								<v-container>
									<v-row>
										<v-col v-for="subject in subjects" :key="subject.id" cols="12" lg="4">
											{{ subject.name }}
										</v-col>
									</v-row>
								</v-container>
							</v-card-text>
						</v-card>
					</v-tabs-window-item>
					<v-tabs-window-item>
						<v-card>
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
									<v-btn @click="updateClassroom()" color="primary">Update</v-btn>
								</v-row>
							</v-card-text>
						</v-card>
					</v-tabs-window-item>
				</v-tabs-window>
			</v-col>
		</v-row>
		<v-row>
			<v-col>
				<v-card>
					<v-card-title>
						Teachers
					</v-card-title>
					<v-card-text>
						<v-data-table :items="classroom.other_teachers" :headers="teacher_headers">
							<template #[`item.id`]="{ item }">
								<router-link :to="{ name: 'Dashboard', params: { id: item} }">
									View Profile
									</router-link>
							</template>
						</v-data-table>
					</v-card-text>
				</v-card>
			</v-col>
			<v-col>
				<v-card>
					<v-card-title>
						Students
					</v-card-title>
					<v-card-text>
						<v-data-table :items="classroom.students" :headers="student_headers">
							<template #[`item.id`]="{ item }">
								<router-link :to="{ name: 'Dashboard', params: { id: item} }">
									View Profile
									</router-link>
							</template>
						</v-data-table>
					</v-card-text>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>

import api from '@/services/api'

export default {
	components: {
	},
	data() {
		return {
			tabs: null,
			classroom: null,
			subjects: [],
			teacher_headers: [
				{ title: 'Name', value: 'user.first_name' },
				{ title: 'Profile', key: 'id', value: teacher => `app/teachers/${teacher.id}` },
			],
			student_headers: [
				{ title: 'Name', value: 'user.first_name' },
				{ title: 'Profile', key: 'id', value: teacher => `app/teachers/${teacher.id}` },
			],
			images: [
				require('@/assets/classrooms/classroom1.png'),
				require('@/assets/classrooms/classroom2.png'),
				require('@/assets/classrooms/classroom3.png'),
			],
		};
	},
	props: ['id'],
	methods: {
		getRandomClassroomImage() {
			const index = Math.floor(Math.random() * this.images.length);
			return this.images[index];
		},
		async updateClassroom() {
			await api.put(`api/allocation/classrooms/${this.id}/`, this.classroom);
		},
		async getClassroomData() {
			this.classroom = (await api.get(`api/allocation/classrooms/${this.id}`)).data;
			this.subjects = (await api.get(`api/allocation/subjects/all?classroom=${this.id}`)).data;
			this.classroom.other_teachers = await Promise.all(this.classroom.other_teachers.map(async (teacher_id) => {
				return (await api.get(`api/accounts/teachers/${teacher_id}/`)).data;
			}));
			this.classroom.students = await Promise.all(this.classroom.students.map(async (student_id) => {
				return (await api.get(`api/accounts/students/${student_id}/`)).data;
			}));
			console.log(this.classroom);
		},
	},
	mounted() {
		this.getClassroomData();
	}
}
</script>
