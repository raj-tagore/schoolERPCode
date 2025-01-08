<template>
	<v-container v-if="this.subject">
		<v-row align="center" justify="center">
			<v-col>
				<v-card>
					<v-tabs
						background-color="deep-purple accent-4"
						center-active
						dark
						align-tabs="center"
						v-model="tabs"
					>
						<v-tab>Overview</v-tab>
						<v-tab>Settings</v-tab>
					</v-tabs>
				</v-card>
				<v-tabs-window v-model="tabs">
					<v-tabs-window-item>
						<v-row class="ma-4">
							<v-col cols="12" lg="4">
								<v-card>
									<v-card-title>
										{{this.subject.name}}
										<p class="text-body-2 pb-4">
											<b>Name: </b>{{this.subject.name}} <br>
											<b>Description: </b>{{ this.subject.description }}
										</p>
									</v-card-title>
								</v-card>
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
										<v-text-area label="Description" v-model="subject.description"></v-text-area>
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

export default {
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
