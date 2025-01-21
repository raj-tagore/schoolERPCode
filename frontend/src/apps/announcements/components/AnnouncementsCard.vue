<template>
    <v-card>
        <v-card-title>Announcements</v-card-title>
        <v-card-text>
            <v-card v-for="(Announcement, index) in AnnouncementsData"
            :key="index" class="my-4">
                <v-card-title class="text-body-2">{{ Announcement.title }}</v-card-title>
                <v-card-subtitle>{{ Announcement.description }}</v-card-subtitle>
                <v-card-text class="text-grey-darken-2">
                    <p>Signed by: {{ Announcement.signed_by.user.full_name }}</p>
                </v-card-text>
            </v-card>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '@/services/api';

const props = defineProps({
  url: String
});

const AnnouncementsData = ref([]);

const getAnnouncementsData = async () => {
  const response = await api.get(props.url);
  AnnouncementsData.value = response.data;
};

onMounted(() => {
  getAnnouncementsData();
});
</script>
