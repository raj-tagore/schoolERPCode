<template>
    <v-container>
        <v-row>
            <v-col>
                <v-card>
                    <v-tabs
                    background-color="deep-purple accent-4"
                    center-active
                    dark
                    density="comfortable"
                    align-tabs="center"
                    v-model="tabs">
                        <v-tab>View</v-tab>
                        <v-tab>Edit</v-tab>
                    </v-tabs>
                </v-card>
                <v-tabs-window v-model="tabs">
                    <v-tabs-window-item>
                        <v-container>
                            <v-card>
                                <v-card-title>{{ announcement?.title }}</v-card-title>
                            </v-card>
                        </v-container>
                    </v-tabs-window-item>
                </v-tabs-window>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { getAnnouncement } from '../api';
import { onMounted, ref } from "vue";

let announcement = ref(null);

const props = defineProps({
    announcementId: Number,
});

onMounted(
    async () => {
        announcement.value = await getAnnouncement(props.announcementId);
    }
);

</script>