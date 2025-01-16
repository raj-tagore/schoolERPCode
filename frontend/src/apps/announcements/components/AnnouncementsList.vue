<template>
    <v-card>
        <v-card-title>Announcements</v-card-title>
        <v-card-text>
            <v-list lines="two" density="default">
                <v-list-item 
                    v-for="(announcement, index) in AnnouncementsData" 
                    :key="index"
                    class="ma-2 pa-2 border"
                >
                    <v-list-item-content>
                        <v-list-item-title >{{ announcement.title }}</v-list-item-title>
                        <v-list-item-subtitle class="mb-2">{{ announcement.description }}</v-list-item-subtitle>
                        <v-list-item-text class="text-end">
                            <p>Signed by: {{ announcement.signed_by.user.full_name }}</p>
                        </v-list-item-text>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '@/services/api';

// Props
const props = defineProps({
    url: String, // URL for fetching announcements
});

const AnnouncementsData = ref([]); // Reactive data for announcements

const getAnnouncementsData = async () => {
    try {
        const response = await api.get(props.url);
        AnnouncementsData.value = response.data;
    } catch (error) {
        console.error("Error fetching announcements:", error);
    }
};

onMounted(getAnnouncementsData);
</script>
