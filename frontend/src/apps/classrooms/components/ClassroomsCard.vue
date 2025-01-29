<template>
    <v-card variant="flat">
        <v-card-text>
            <v-row>
                <v-col 
                v-for="classroom in classrooms" 
                :key="classroom.id" 
                cols="6" 
                md="3" 
                lg="2"
                >
                    <v-card>
                        <v-img 
                            :src="getClassroomImage()" 
                            class="custom-img"
                        ></v-img>
                        <v-card-title class="text-body-1">{{ classroom.name }}</v-card-title>
                        <v-card-subtitle>{{ classroom.class_teacher_details?.user_details?.full_name || "Loading..." }}</v-card-subtitle>
                        <v-card-actions class="d-flex justify-center">
                            <v-btn :to="{ name: 'Classroom', params: { classroomId: classroom.id }}">Enter Class</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { ref, watch } from "vue";
import { getClassrooms, getClassroomImage } from "../api";

const props = defineProps({
	filter: {
		type: Object,
		default: () => ({}),
	},
});

const classrooms = ref([]);

const fetchClassrooms = async () => {
	classrooms.value = (await getClassrooms(props.filter)).results;
};

// Watch for changes in the filter
watch(() => props.filter, fetchClassrooms, { deep: true });

// Initial fetch
fetchClassrooms();
</script>

<style>
.custom-img {
	aspect-ratio: 16/9;
	object-fit: cover;
	width: 100%;
	height: auto;
}
</style>
  
