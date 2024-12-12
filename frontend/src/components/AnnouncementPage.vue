<template>
	<div>
		<h1>
			Announcements
		</h1>
	</div>
	<v-container>
		<v-row v-if="announcements.length>0" dense>
			<v-col v-for="(announcement) in announcements" :key="announcement.id" cols="12" sm="6" md="4">
				<v-card class="mb-3" outlined> 
					<v-card-title>{{ announcement.title }}</v-card-title>
					<v-card-subtitle>Priority: {{ announcement.priority }}</v-card-subtitle>
					<v-card-text>
						<p>{{ announcement.description }}</p>

						<div v-if="announcement.classrooms && announcement.classrooms.length">
						<strong>Classrooms:</strong>
						<ul>
							<li v-for="(classroom, cIndex) in announcement.classrooms" :key="cIndex">
							{{ classroom }}
							</li>
						</ul>
						</div>

						<!-- Show Subjects if available -->
						<div v-if="announcement.subjects && announcement.subjects.length">
						<strong>Subjects:</strong>
						<ul>
							<li v-for="(subject, sIndex) in announcement.subjects" :key="sIndex">
							{{ subject }}
							</li>
						</ul>
						</div>

						<!-- Signed By -->
						<div v-if="announcement.signed_by">
						<strong>Signed By (ID):</strong> {{ announcement.signed_by }}
						</div>
					</v-card-text>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import api from '@/services/api';

export default {
	name: 'AnnouncementPage',
	data() {
		return {
			announcements: [],
		};
	},
	mounted() {
		this.fetchAnnouncements();
	},
	methods: {
		async fetchAnnouncements() {
			try {
				const response = await api.get('/api/announcements');
				this.announcements = response.data;
			} catch (error) {
				console.error('Error fetching announcements:', error);
			}
		}
	}

}
</script>
