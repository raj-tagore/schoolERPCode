<template>
  <v-card>
    <v-card-title>
      <v-row>
        <v-col cols="4">
          <v-text-field
            v-model="filters.title"
            label="Search by title"
            density="comfortable"
            @input="fetchAnnouncements"
          ></v-text-field>
        </v-col>
        <v-col cols="4">
          <v-autocomplete
            v-model="filters.classroom"
            :items="classrooms"
            label="Filter by classroom"
            :item-props="getClassroomInfoFromObj"
            clearable
            @update:model-value="fetchAnnouncements"
          ></v-autocomplete>
        </v-col>
        <v-col cols="4">
          <v-autocomplete
            v-model="filters.subject"
            :items="subjects"
            label="Filter by subject"
            :item-props="getSubjectInfoFromObj"
            clearable
            @update:model-value="fetchAnnouncements"
          ></v-autocomplete>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-autocomplete
            v-model="filters.signed_by"
            :items="teachers"
            label="Filter by signer"
            :item-props="getTeacherInfoFromObj"
            clearable
            @update:model-value="fetchAnnouncements"
          ></v-autocomplete>
        </v-col>
        <v-col cols="6">
          <v-select
            v-model="filters.is_school_wide"
            :items="[
              { title: 'All Announcements', value: null },
              { title: 'School Wide Only', value: 'True' },
              { title: 'Non-School Wide Only', value: 'False' }
            ]"
            label="School Wide Filter"
            @update:model-value="fetchAnnouncements"
          ></v-select>
        </v-col>
      </v-row>
    </v-card-title>

    <v-data-table
      :headers="headers"
      :items="announcements"
      :loading="loading"
      class="elevation-1"
    >
      <template #item.release_at="{ item }">
        {{ formatDate(item.release_at) }}
      </template>
      <template #item.expiry_at="{ item }">
        {{ formatDate(item.expiry_at) }}
      </template>
      <template #item.signed_by="{ item }">
        {{ item.signed_by?.user.full_name }}
      </template>
      <template #item.actions="{ item }">
        <v-btn
          icon="mdi-eye"
          size="small"
          variant="text"
          :to="{ name: 'Announcement', params: { announcementId: item.id }}"
        ></v-btn>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getAnnouncements } from "../api";
import { getClassrooms, getClassroomInfoFromObj } from "@/apps/classrooms/api";
import { getSubjects, getSubjectInfoFromObj } from "@/apps/subjects/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/users/api";

const announcements = ref([]);
const classrooms = ref([]);
const subjects = ref([]);
const teachers = ref([]);
const loading = ref(false);

const filters = ref({
  title: "",
  classroom: null,
  subject: null,
  signed_by: null,
  is_school_wide: null
});

const headers = [
  { title: "Title", key: "title" },
  { title: "Release Date", key: "release_at" },
  { title: "Expiry Date", key: "expiry_at" },
  { title: "Signed By", key: "signed_by" },
  { title: "Actions", key: "actions", sortable: false },
];

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
};

const fetchAnnouncements = async () => {
  loading.value = true;
  try {
    const filterParams = {};
    
    if (filters.value.title) filterParams.title = filters.value.title;
    if (filters.value.classroom) filterParams.classroom = filters.value.classroom;
    if (filters.value.subject) filterParams.subject = filters.value.subject;
    if (filters.value.signed_by) filterParams.signed_by = filters.value.signed_by;
    if (filters.value.is_school_wide) filterParams.is_school_wide = filters.value.is_school_wide;

    // Only fetch if at least one filter is active
    if (Object.keys(filterParams).length > 0) {
      announcements.value = await getAnnouncements(filterParams);
    } else {
      announcements.value = [];  // Clear the table when no filters
    }
  } catch (error) {
    console.error("Error fetching announcements:", error);
  } finally {
    loading.value = false;
  }
};

onMounted(async () => {
  classrooms.value = await getClassrooms();
  subjects.value = await getSubjects();
  teachers.value = await getTeachers();
  // Don't fetch announcements on mount, start with empty table
  announcements.value = [];
});
</script>
