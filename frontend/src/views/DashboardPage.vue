<template>
  <v-container>
  <v-row>
    <v-col cols="12" lg="4">
      <AnnouncementsList 
      title="School-wide Announcements"
      subtitle="Important announcements for all students and staff"
      :filter="{ 'is_school_wide': 'True' }"
    />
    </v-col>
  </v-row>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue';
import AnnouncementsList from '@/apps/announcements/components/AnnouncementsList.vue';

export default defineComponent({
  components: {
    AnnouncementsList,
  },
  setup() {
    return {};
  },
});

</script>
