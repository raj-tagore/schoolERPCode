<template>
  <v-container>
    <v-row align="center" justify="center" v-if="subject">
    <v-col>
        <v-row class="ma-2">
          <v-col cols="12" lg="4">
            <SubjectCard :subject="subject"></SubjectCard>
          </v-col>
          <v-col cols="12" lg="4" v-if="subject">
            <AnnouncementsList :filter="{ subject: subject.id }" :to="`SubjectAnnouncements`" :title="`Announcements`" />
          </v-col>
        </v-row>
    </v-col>
    </v-row>
  </v-container>
</template>
  
<script setup>
import { ref, onMounted } from "vue";
import { api } from "@/services/api";
import SubjectCard from "@/apps/subjects/components/SubjectCard.vue";
import AnnouncementsList from "@/apps/announcements/components/AnnouncementsList.vue";
import { getTeachers } from "@/apps/teachers/api";

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
  
