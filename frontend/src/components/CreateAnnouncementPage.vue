<template>
	<v-app>
		<v-main>
			<v-container>
				<h2>
					Create Announcement
				</h2>
				<v-form @submit.prevent="createAnnouncementHandler()">
					<v-text-field v-model="title" label="Title" required outlined></v-text-field>
					<v-text-field v-model="description" label="Description" required outlined></v-text-field>
					<v-date-input v-model="release_date" label="Release Date" required outlined></v-date-input>
					<v-date-input v-model="expiry_date" label="Expiry Date" required outlined></v-date-input>
					<v-btn color="primary" type="submit" class="mt-4">Create Announcement</v-btn>
				</v-form>
			</v-container>
		</v-main>
	</v-app>
</template>

<script>
import { mapActions } from 'vuex';

export default {
	data() {
		return {
			title: '',
			description: '',
			release_date: Date.now(),
			expiry_date: new Date(Date.now() + (24 * 60 * 60 * 1000)),
		};
	},
	methods: {
		...mapActions(['createAnnouncement']),
		async createAnnouncementHandler() {
			try {
				const result = await this.createAnnouncement({
					title: this.title,
					description: this.description,
					release_date: new Date(this.release_date).toISOString(),
					expiry_date: new Date(this.expiry_date).toISOString(),
				})
				if (result) {
					alert('Announcement created successfully');
					this.$router.push({ name: 'Dashboard' });
				}
			} catch (err) {
				this.error = (err.response && err.response.data.detail) || 'Creation of accouncement failed';
			}
		} 
	}
}
</script>
