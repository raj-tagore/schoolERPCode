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
					<v-select v-model="priority" :item-props="itemProps" label="Priority" :items="['low', 'medium', 'high']" required outlined></v-select>
					<v-btn color="primary" type="submit" class="mt-4">Create Announcement</v-btn>
				</v-form>
			</v-container>
		</v-main>
	</v-app>
</template>

<script setup>
const itemProps = (item) => ({title: item.charAt(0).toUpperCase() + item.slice(1) + " Priority"})
</script>

<script>

import api from '@/services/api';

export default {
	data() {
		return {
			title: '',
			description: '',
			release_date: Date.now(),
			expiry_date: new Date(Date.now() + (24 * 60 * 60 * 1000)),
			priority: 'low',
		};
	},
	methods: {
		async createAnnouncement(_, announcement) {
			console.log(announcement)
			const resp = await api.post('api/announcements/', announcement);
			if (!resp || !resp.ok) {
				throw new Error("Failed to create announcement");
			}
			return true;
			},
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
