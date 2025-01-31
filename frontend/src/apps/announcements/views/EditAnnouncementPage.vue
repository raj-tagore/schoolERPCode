<template>
	<v-container>
		<v-row>
			<v-col>
				<AnnouncementSettingsCard :announcementId="announcementId"></AnnouncementSettingsCard>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>

import AnnouncementSettingsCard from "@/apps/announcements/components/AnnouncementSettingsCard.vue";

const props = defineProps({
	announcementId: Number,
});

</script>
