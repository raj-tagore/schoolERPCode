<template>
    <v-card>
        <v-card-title v-if="title">{{ title }}</v-card-title>
        <v-card-subtitle v-if="subtitle">{{ subtitle }}</v-card-subtitle>
        <v-card-text>
            <v-list lines="two" density="default">
                <v-list-item 
                    v-for="(announcement, index) in AnnouncementsData.slice(0, 3)" 
                    :key="index"
                    class="ma-1 pa-2 border"
                >
                    <v-list-item-content>
                        <v-list-item-title>{{ announcement?.title || 'Untitled' }}</v-list-item-title>
                        <v-list-item-subtitle class="mb-2">{{ announcement?.description || 'No description available' }}</v-list-item-subtitle>
                        <v-list-item-text class="text-end">
                            <p>Signed by: {{ announcement?.signed_by_details?.user_details?.full_name || 'Unknown' }}</p>
                        </v-list-item-text>
                    </v-list-item-content>
                    <template v-slot:append>
                        <v-btn 
                            v-if="announcement"
                            icon="mdi-arrow-right"
                            variant="flat"
                            border
                            density="comfortable"
                            :to="{ name: 'Announcement', params: { announcementId: announcement.id } }"
                        ></v-btn>
                    </template>
                </v-list-item>
            </v-list>
            <div v-if="!AnnouncementsData?.length" class="text-center pa-4">
                No announcements available
            </div>
        </v-card-text>
        <v-card-actions class="justify-center">
            <v-btn 
                :to="{ name: to || 'Announcements' }"
                variant="outlined"
                density="comfortable"
            >
                View All
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getAnnouncements } from "@/apps/announcements/api";

const props = defineProps({
	filter: {
		type: Object,
		default: () => ({}),
	},
	title: String,
	subtitle: String,
    to: String,
});

const AnnouncementsData = ref([]);

onMounted(async () => {
	AnnouncementsData.value = (await getAnnouncements(props.filter)).results;
});
</script>
