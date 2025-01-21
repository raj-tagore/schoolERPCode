<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-tabs background-color="deep-purple accent-4" center-active dark density="comfortable" align-tabs="center"
            v-model="tabs">
            <v-tab>View</v-tab>
            <v-tab>Edit</v-tab>
          </v-tabs>
        </v-card>
        <v-tabs-window v-model="tabs">
          <v-tabs-window-item>
            <v-row class="ma-2">
              <v-col lg="6">
                <v-card>
                  <v-card-title>{{ announcement?.title }}</v-card-title>
                  <v-card-subtitle>{{ announcement?.signed_by?.user?.full_name }}</v-card-subtitle>
                  <v-card-text>{{ announcement?.description }}</v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-tabs-window-item>
        </v-tabs-window>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "@/services/api";

let announcement = ref({});
const tabs = ref(null);
const props = defineProps({
  announcementId: Number,
});

const getAnnouncement = async () => {
  announcement.value = (await api.get(`api/announcements/${props.announcementId}`)).data
}

onMounted(
  async () => {
    getAnnouncement();
  }
);

</script>