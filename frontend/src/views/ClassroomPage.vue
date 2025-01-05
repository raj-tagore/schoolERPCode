<template>
  <v-container>
    <v-row>
      <v-col cols="1" lg="6">
		<v-card v-if="classroomData" prepend-avatar="https://placehold.co/600x400">
			<v-card-title>
				{{ classroomData.name }} - {{ classroomData.section }}
			</v-card-title>
			<v-card-subtitle>
				{{ classroomData.class_teacher_name || "Loading..." }}
			</v-card-subtitle>
			<v-card-actions>
				<span v-if="classroomLink">
					<v-btn :href="classroomLink">Classroom Invite Link</v-btn>
					<v-btn @click="generateClassroomLink">Refresh Invite Link</v-btn>
				</span>
				<v-btn v-else @click="generateClassroomLink">Generate Link</v-btn>
			</v-card-actions>
		</v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from "@/services/api";
import { useRouter } from "vue-router";

export default {
	data() {
		return {
			classroomData: null,
			classroomLink: null,
		};
	},
	methods: {
		async getClassroomData() {
			const classroomId = this.$route.params.id;
			const router = useRouter();
			if (!classroomId) {
				router.push({ name: "Dashboard" });
				return;
			}
			const response = await api.get(
				`api/allocation/classrooms/?id=${classroomId}`,
			);
			this.classroomData = response.data;

			this.classroomData;
			if (!this.classroomData.class_teacher) {
				return;
			}
			const teacherResponse = await api.get(
				`api/accounts/all/?id=${this.classroomData.class_teacher}`,
			);
			this.classroomData.class_teacher_name = `${teacherResponse.data[0].first_name} ${teacherResponse.data[0].last_name}`;
		},
		async generateClassroomLink() {
			const classroomLinkData = await api.post(
				"api/allocation/classrooms/generate_link/",
				{
					id: this.classroomData.id,
				},
			);
			this.classroomLink = `${window.location.origin}/classroom/join?id=${classroomLinkData.id}`;
		},
		async getTeacherName(id) {
			const response = await api.get(`api/accounts/all/?id=${id}`);
			return `${response.data.first_name} ${response.data.last_name}`;
		},
	},
	mounted() {
		this.getClassroomData();
	},
};
</script>
