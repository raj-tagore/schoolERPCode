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
            <v-row class="ma-2 flex justify-center">
              <v-col lg="4">
                <v-card>
                  <v-card-title>{{ announcement?.title }}</v-card-title>
                  <v-card-text>
                    {{ announcement?.description }}
                    <h4 class="text-subtitle-1 mt-4">Signed by:</h4>
                    <v-list lines="2">
                      <v-list-item 
                        :title="announcement?.signed_by?.user.full_name"
                        :subtitle="announcement?.signed_by?.user.email"
                        :variant="'flat'"
                        rounded="lg"
                        :to="'#'"
                      />
                    </v-list>
                    <h4 class="text-subtitle-1 mt-4">Dates:</h4>
                    <v-chip color="primary">Release: {{ formatDate(announcement.release_at) }}</v-chip>
                    <v-chip color="red">Expiry: {{ formatDate(announcement.expiry_at) }}</v-chip>
                  </v-card-text>
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

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });
};

onMounted(
  async () => {
    getAnnouncement();
  }
);

</script>