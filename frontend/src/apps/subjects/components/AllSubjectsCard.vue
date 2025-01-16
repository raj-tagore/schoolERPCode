<template>
<v-container>
    <v-card>
        <v-row class="ma-2">
            <v-col 
            v-for="(classroom, index) in classroomsData" 
            cols="12" lg="4" md="6"
            :key="index">
                <SubjectsCard :filter="{ classroom: classroom.id }"/>
            </v-col>
        </v-row>
    </v-card>
</v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getClassrooms } from "@/apps/classrooms/api";
import SubjectsCard from "@/apps/subjects/components/SubjectsCard"

const classroomsData = ref([])

const fetchClassroomsData = async () => {
    classroomsData.value = await getClassrooms();
};
onMounted(fetchClassroomsData);
</script>

