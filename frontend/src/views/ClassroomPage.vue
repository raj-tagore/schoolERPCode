<template>
	<v-container>
		<v-row>
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
						<v-card v-if="this.classroom">
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
						</v-card>
					</v-tabs-window-item>
				</v-tabs-window>
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
		async getClassroomData() {
			const classroomResponse = await api.get(`api/allocation/classrooms/${this.id}`);
			this.classroom = classroomResponse.data;
			const subjectsResponse = await api.get(`api/allocation/subjects/all?classroom=${this.id}`);
			this.subjects = subjectsResponse.data;
		},
	},
	mounted() {
		this.getClassroomData();
	}
}
</script>
