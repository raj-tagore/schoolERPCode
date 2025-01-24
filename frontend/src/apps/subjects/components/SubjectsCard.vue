<template>
    <v-card>
        <v-card-title>Subjects</v-card-title>
        <v-card-text>
            <v-row>
            <v-col 
            v-for="(subject, index) in subjects" 
            :key="index" 
            cols="6" >
                <v-card>
                <v-card-title class="text-body-1 pb-0">{{ subject.name }}</v-card-title>
                <v-card-subtitle>{{ subject.teacher_details?.user?.full_name }}</v-card-subtitle>
                <v-card-actions class="d-flex justify-center">
                    <v-btn :to="{ name: 'Subject', params: { subjectId: subject.id }}">Enter</v-btn>
                </v-card-actions>
                </v-card>
            </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getSubjects } from "../api"

// Props
const props = defineProps({
  filter: Object, 
});

let subjects = ref([]);
const fetchSubjects = async () => {
  subjects.value = await getSubjects(props.filter);
};
onMounted(fetchSubjects);
</script>

      
