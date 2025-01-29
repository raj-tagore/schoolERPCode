<template>
	<v-container>
	  <v-row align="center" justify="center" v-if="subject">
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
				  <AnnouncementsList :filter="{ subject: subject.id }" />
				</v-col>
			  </v-row>
			</v-tabs-window-item>
			<v-tabs-window-item>
				<v-row class="ma-2">
					<v-col lg="4">
						<SubjectSettingsCard v-if="subject" :subject="subject"/>
					</v-col>
				</v-row>
			</v-tabs-window-item>
		  </v-tabs-window>
		</v-col>
	  </v-row>
	</v-container>
</template>
  
<script setup>
import { ref, onMounted } from "vue";
import { api } from "@/services/api";
import SubjectCard from "@/apps/subjects/components/SubjectCard.vue";
import AnnouncementsList from "@/apps/announcements/components/AnnouncementsList.vue";
import { getTeachers } from "@/apps/users/api";
import SubjectSettingsCard from "../components/SubjectSettingsCard.vue";

const props = defineProps({
	subjectId: String,
});

const tabs = ref(null);
const teachers = ref([]);
const subject = ref({});

const getSubjectData = async () => {
	subject.value = (
		await api.get(`api/allocation/subjects/${props.subjectId}`)
	).data;
};

onMounted(async () => {
	getSubjectData();
	teachers.value = (await getTeachers()).results;
});
</script>
  
