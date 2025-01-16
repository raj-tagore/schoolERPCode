<template>
<v-container>
    <v-card>
        <v-row class="ma-2">
            <v-col 
            v-for="(classroom, index) in classroomsData" 
            cols="12" lg="3" md="6"
            :key="index">
                <SubjectsList :filter="{ classroom: classroom.id }" :title="classroom.name"/>
            </v-col>
        </v-row>
    </v-card>
</v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getClassrooms } from "@/apps/classrooms/api";
import SubjectsList from "@/apps/subjects/components/SubjectsList"

const classroomsData = ref([])
const fetchClassroomsData = async () => {
    classroomsData.value = await getClassrooms();
};
onMounted(fetchClassroomsData);
</script>

