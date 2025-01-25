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
            @input="fetchAnnouncements"
            hide-details
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4" lg="3">
          <v-autocomplete
            v-model="filters.classroom"
            :items="classrooms"
            label="Filter by classroom"
            :item-props="getClassroomInfoFromObj"
            clearable
            @update:model-value="fetchAnnouncements"
            hide-details
          ></v-autocomplete>
        </v-col>
        <v-col cols="12" md="4" lg="3">
          <v-autocomplete
            v-model="filters.subject"
            :items="subjects"
            label="Filter by subject"
            :item-props="getSubjectInfoFromObj"
            clearable
            @update:model-value="fetchAnnouncements"
            hide-details
          ></v-autocomplete>
        </v-col>
        <v-col cols="12" md="4" lg="3">
          <v-autocomplete
            v-model="filters.signed_by"
            :items="teachers"
            label="Filter by signer"
            :item-props="getTeacherInfoFromObj"
            clearable
            @update:model-value="fetchAnnouncements"
            hide-details
          ></v-autocomplete>
        </v-col>
        <v-col cols="12" md="4" lg="3">
          <v-select
            v-model="filters.is_school_wide"
            :items="[
              { title: 'All Announcements', value: null },
              { title: 'School Wide Only', value: 'True' },
              { title: 'Non-School Wide Only', value: 'False' }
            ]"
            label="School Wide Filter"
            @update:model-value="fetchAnnouncements"
            hide-details
          ></v-select>
        </v-col>
      </v-row>
    </v-card-title>

    <!-- Mobile view: Cards -->
    <div class="d-md-none">
      <v-card
        v-for="item in announcements"
        :key="item.id"
        class="ma-2 pa-2"
        variant="outlined"
      >
        <div class="d-flex align-center justify-space-between">
          <v-card-title class="text-subtitle-1">{{ item.title }}</v-card-title>
          <v-btn
            icon="mdi-arrow-right"
            size="small"
            variant="outlined"
            :to="{ name: 'Announcement', params: { announcementId: item.id }}"
          ></v-btn>
        </div>
        <v-card-text>
          <div class="d-flex flex-column gap-1">
            <div class="d-flex align-center justify-space-between">
              <span class="text-caption">Release:</span>
              <span>{{ formatDate(item.release_at) }}</span>
            </div>
            <div class="d-flex align-center justify-space-between">
              <span class="text-caption">Expiry:</span>
              <span>{{ formatDate(item.expiry_at) }}</span>
            </div>
            <div class="d-flex align-center justify-space-between">
              <span class="text-caption">Signed By:</span>
              <span>{{ item.signed_by?.user.full_name }}</span>
            </div>
          </div>
        </v-card-text>
      </v-card>
    </div>

    <!-- Desktop view: Data Table -->
    <v-data-table
      class="d-none d-md-block"
      :headers="headers"
      :items="announcements"
      :loading="loading"
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
          icon="mdi-arrow-right"
          size="small"
          variant="outlined"
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
