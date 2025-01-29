<template>
  <v-card variant="flat">
    <v-card-title>
      <!-- Search filters -->
      <v-row>
        <v-col cols="12" md="4" lg="3">
          <v-text-field
            v-model="filters.title"
            label="Search by title"
            density="comfortable"
            hide-details
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4" lg="2">
          <v-autocomplete
            v-model="filters.classroom"
            :items="classrooms"
            label="Filter by classroom"
            :item-props="getClassroomInfoFromObj"
            clearable
            hide-details
            density="comfortable"
          ></v-autocomplete>
        </v-col>
        <v-col cols="12" md="4" lg="2">
          <v-autocomplete
            v-model="filters.subject"
            :items="subjects"
            label="Filter by subject"
            :item-props="getSubjectInfoFromObj"
            clearable
            hide-details
            density="comfortable"
          ></v-autocomplete>
        </v-col>
        <v-col cols="12" md="4" lg="3">
          <v-autocomplete
            v-model="filters.signed_by"
            :items="teachers"
            label="Filter by signer"
            :item-props="getTeacherInfoFromObj"
            clearable
            hide-details
            density="comfortable"
          ></v-autocomplete>
        </v-col>
        <v-col cols="12" md="4" lg="2">
          <v-select
            v-model="filters.is_school_wide"
            :items="[
            { title: 'All Announcements', value: null },
            { title: 'School Wide Only', value: 'True' },
            { title: 'Non-School Wide Only', value: 'False' }
            ]"
            label="School Wide Filter"
            hide-details
            density="comfortable"
          ></v-select>
        </v-col>
      </v-row>
    </v-card-title>

		<ResponsiveDataTable 
			:getToFunction="(item) => ({name: 'Announcement', params: {announcementId: item.id}})" 
			:headers="headers" 
			:fetch="getAnnouncements" 
			:filters="filters"></ResponsiveDataTable>

  </v-card>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getAnnouncements } from "../api";
import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import { getSubjects, getSubjectInfoFromObj } from "@/apps/subjects/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/users/api";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";

const classrooms = ref([]);
const subjects = ref([]);
const teachers = ref([]);

const filters = ref({
	title: "",
	classroom: null,
	subject: null,
	signed_by: null,
	is_school_wide: null,
});

const formatDate = (dateString) => {
	return new Date(dateString).toLocaleString("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
	});
};

const headers = [
	{ title: "Title", key: "title" },
	{ title: "Release Date", key: "release_at", formatFunc: formatDate },
	{ title: "Expiry Date", key: "expiry_at", formatFunc: formatDate },
	{
		title: "Signed By",
		key: "signed_by_details",
		formatFunc: (signedBy) => signedBy.user_details.full_name,
	},
	{ title: "Actions", key: "actions", sortable: false },
];

onMounted(async () => {
	classrooms.value = (await getClassrooms()).results;
	subjects.value = (await getSubjects()).results;
	teachers.value = (await getTeachers()).results;
	// Don't fetch announcements on mount, start with empty table
});
</script>
