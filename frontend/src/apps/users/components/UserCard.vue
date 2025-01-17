<template>
	<v-container v-if="user">
		<v-row>
			<v-col>
				<v-card>
					<v-card-title>
						<v-avatar>
							<v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" />
						</v-avatar>
						<v-card-title>
							{{user.full_name}}
						</v-card-title>
						<v-card-subtitle>
							{{user.account.type}}
						</v-card-subtitle>
						<v-card-text>
							Overview
							<v-spacer />
							Email: {{user.email}}
						</v-card-text>
					</v-card-title>
				</v-card>
			</v-col>
			<v-col>
				<v-card v-if="classrooms">
					<v-card-title>
						<v-card-title>
							Classrooms
						</v-card-title>
						<v-card-text>
							<v-row v-for="classroom in classrooms">
								<v-card density="compact">
									<v-card-text>
										<v-row>
											<v-col>
												{{classroom.name}} - 
												{{classroom.standard}}
											</v-col>
											<v-col>
												<v-btn class="mx-2" size="x-small" icon="mdi-eye" :to="{ name: 'Classroom', params: { classroomId: classroom.id }}"></v-btn>
											</v-col>
										</v-row>
									</v-card-text>
								</v-card>
							</v-row>
						</v-card-text>
					</v-card-title>
				</v-card>
			</v-col>
			<v-col>
				<AnnouncementsList :url="announcementUrl" />
			</v-col>
		</v-row>

	</v-container>
</template>


<script setup>
import { ref, onMounted, computed } from "vue";

import api from "@/services/api";

import { getClassrooms } from "@/apps/classrooms/api";
import AnnouncementsList from "@/apps/announcements/components/AnnouncementsList.vue";

const props = defineProps({
	userId: Number,
});

const user = ref(null);

const classrooms = ref(null);

const filter = ref({});

const announcementUrl = computed({
	get: () => {
		return `api/announcements/all/?${(new URLSearchParams(filter.value)).toString()}`;
	},
});

onMounted(async () => {
	user.value = (await api.get(`api/users/${props.userId}/`)).data;
	if (user.value.account.type === "Teacher") {
		filter.value.other_teachers = user.value.account.id;
	} else if (user.value.account.type === "Student") {
		filter.value.students = user.value.account.id;
	}
	classrooms.value = await getClassrooms(filter.value);
});
</script>
