<template>
	<v-container>
	<v-row align="center" justify="center" v-if="this.subject">
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
				</v-tabs>
			</v-card>
			<v-tabs-window v-model="tabs">
				<v-tabs-window-item>
					<v-row class="ma-2">
						<v-col cols="12" lg="4">
							<SubjectCard :subject="subject"></SubjectCard>
						</v-col>
						<v-col cols="12" lg="4" v-if="subject.id">
							<AnnouncementCards :url="`api/announcements/all/?subject=${subject.id}`" />
						</v-col>
					</v-row>
				</v-tabs-window-item>
				<v-tabs-window-item>
					<v-card class="ma-4 pa-4">
						<v-card-title>Settings</v-card-title>
						<v-card-text>
							<v-row>
								<v-col cols="12" lg="6">
									<v-text-field label="Name" v-model="subject.name"></v-text-field>
								</v-col>
							</v-row>
							<v-row>
								<v-col cols="12" lg="6">
									<v-textarea label="Description" v-model="subject.description"></v-textarea>
								</v-col>
							</v-row>
							<v-row>
								<v-col cols="12" lg="6">
									<v-autocomplete label="Teacher" :item-props="teacherInfoFromObj" :items="teachers" v-model="subject.teacher"></v-autocomplete>
								</v-col>
								<v-col cols="12" lg="6">
									<v-checkbox label="Is Active" v-model="subject.is_active"></v-checkbox>
								</v-col>
								</v-row>
							<v-row>
								<v-btn @click="updateSubject()" color="primary">Update</v-btn>
							</v-row>
						</v-card-text>
					</v-card>
				</v-tabs-window-item>
			</v-tabs-window>
		</v-col>
	</v-row>
	</v-container>
</template>

<script>
import api from "@/services/api";
import SubjectCard from "@/subjects/components/SubjectCard.vue";
import AnnouncementCards from "@/announcements/components/AnnouncementsCard.vue";

export default {
	components: {
		SubjectCard,
		AnnouncementCards,
	},
	data() {
		return {
			tabs: null,
			teachers: [],
			subject: [],
		};
	},
	props: ["subjectId"],
	methods: {
		async updateSubject() {
			await api.put(`api/allocation/subjects/${this.subjectId}/`, this.subject);
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
		async getSubjectData() {
			this.subject = (
				await api.get(`api/allocation/subjects/${this.subjectId}`)
			).data;
		},
	},
	mounted() {
		this.getSubjectData();
		this.getTeachers();
	},
};
</script>
