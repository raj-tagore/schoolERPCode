<template>
	<v-container>
		<v-row align="center" justify="center" v-if="teacher">
			<v-col>
				<v-card>
					<v-tabs
						background-color="deep-purple accent-4"
						center-active
						dark
						density="comfortable"
						align-tabs="center"
						v-model="tabs"
					>
						<v-tab>Profile</v-tab>
						<v-tab>Settings</v-tab>
					</v-tabs>
				</v-card>
				<v-tabs-window v-model="tabs">
					<v-tabs-window-item>
						<v-row class="ma-2">
							<v-col cols="12" lg="4">
								<ClassroomCard :classroomId="classroomId" />
							</v-col>
							<v-col cols="12" lg="4">
								<SubjectsList :filter="{ classroom: classroom.id }" />
							</v-col>
							<v-col cols="12" lg="4">
								<AnnouncementsList :url="`api/announcements/all/?classroom=${classroom.id}`" />
							</v-col>
						</v-row>
					</v-tabs-window-item>
					<v-tabs-window-item>
						<ClassroomSettings :classroomId="classroomId" />
					</v-tabs-window-item>
				</v-tabs-window>
			</v-col>
		</v-row>

	</v-container>
</template>

<script setup>
import { ref } from 'vue';

import TeacherCard from '@/apps/users/components/TeacherCard.vue';

const teacher = ref(null);
const tabs = ref(null);

const props = defineProps({
	teacherId: Number,
});

</script>
