<template>
	<v-container>
		<v-card class="mb-5 pa-4">
			<v-card-title>Announcements</v-card-title>
			<v-card-text>
				<v-row>
					<v-col v-for="(announcement, index) in announcementsData" :key="index" cols="6">
						<v-card class="pa-1">
							<v-card-title class="text-body-1">{{ announcement.title }}</v-card-title>
							<v-card-subtitle>{{ announcement.content }}</v-card-subtitle>
							<v-card-actions class="d-flex justify-center">
								<v-btn :to="{ name: 'Announcement', params: { announcementId: announcement.id }}">Enter</v-btn>
							</v-card-actions>
						</v-card>
					</v-col>
				</v-row>
			</v-card-text>
		</v-card>
	</v-container>
</template>

<script>
import api from "@/services/api";

export default {
	name: "AnnouncementsCard",
	data() {
		return {
			announcements: [],
		}
	},
	methods: {
		async getAnnouncements(classroomId) {
			
		}
	}
};
</script>
