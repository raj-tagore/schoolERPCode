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
import SubjectCard from "@/components/SubjectCard.vue";
import AnnouncementCards from "@/components/AnnouncementCards.vue";

export default {
	components: {
		SubjectCard,
		AnnouncementCards,
	},
	data() {
		return {
			tabs: null,
			subject: [],
		};
	},
	props: ["subjectId"],
	methods: {
		async updateSubject() {
			await api.put(`api/allocation/subjects/${this.subjectId}/`, this.subject);
		},
		async getSubjectData() {
			this.subject = (
				await api.get(`api/allocation/subjects/${this.subjectId}`)
			).data;
		},
	},
	mounted() {
		this.getSubjectData();
	},
};
</script>
