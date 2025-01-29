<template>
    <v-card>
        <v-card-title>Announcements</v-card-title>
        <v-card-text>
            <v-card v-for="(announcement, index) in announcementsData"
            :key="index" class="my-4">
                <v-card-title class="text-body-2">{{ announcement.title }}</v-card-title>
                <v-card-subtitle>{{ announcement.description }}</v-card-subtitle>
                <v-card-text class="text-grey-darken-2">
                    <p>Signed by: {{ announcement.signed_by_details.user.full_name }}</p>
                </v-card-text>
            </v-card>
        </v-card-text>
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
});

const announcementsData = ref([]);

onMounted(async () => {
	announcementsData.value = (await getAnnouncements(props.filter)).results;
});
</script>
