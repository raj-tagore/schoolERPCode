<template>
    <v-container>
    <v-row>
        <v-col cols="12" lg="4">
            <AnnouncementsList :subtitle="'School Wide'" :url="'api/announcements/all/?is_school_wide=True'"/>
        </v-col>
    </v-row>
</v-container>
</template>

<script setup>
import AnnouncementsList from '../components/AnnouncementsList.vue';

</script>