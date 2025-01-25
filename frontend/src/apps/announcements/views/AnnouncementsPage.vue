<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="4">
        <AnnouncementsList 
          title="School Wide Announcements" 
          :filter="{ 'is_school_wide': 'True' }" 
        />
      </v-col>
      <v-col cols="12" lg="8">
        <AnnouncementsTable />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import AnnouncementsList from '../components/AnnouncementsList.vue';
import AnnouncementsTable from '../components/AnnouncementsTable.vue';

</script>