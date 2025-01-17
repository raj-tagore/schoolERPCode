<template>
<v-container>
    <v-card class="mb-5">
        <v-card-title class="text-h5">Classes</v-card-title>
        <v-card-text>
				<container>
					<v-row>
						<v-col>
						<v-text-field
							v-model="search"
							label="Search for your classroom"
                            density="comfortable"
						/>

						</v-col>
					</v-row>
            <v-row>
            <v-col 
            v-for="(classroom, index) in classroomsData" 
            :key="index" 
            cols="12" 
            sm="4" 
            xl="2" >
                <v-card>
                <v-img 
                    :src="getClassroomImage()" 
                    class="custom-img"
                ></v-img>
                <v-card-title class="text-body-1">{{ classroom.name }}</v-card-title>
				<v-card-subtitle>{{ classroom.class_teacher_details?.user?.full_name || "Loading..." }}</v-card-subtitle>
                <v-card-actions class="d-flex justify-center">
                    <v-btn :to="{ name: 'Classroom', params: { classroomId: classroom.id }}">Enter Class</v-btn>
                </v-card-actions>
                </v-card>
            </v-col>
            </v-row></container>
        </v-card-text>
    </v-card>
</v-container>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { getClassrooms, getClassroomImage } from "../api";

const classroomsDataRaw = ref([]);
const search = ref("");

const classroomsData = computed({
	get: () => {
		console.log(search.value.length);
		if (search.value.length === 0) {
			return classroomsDataRaw.value;
		}
		return classroomsDataRaw.value.filter((v) =>
			`${v.name}${v.standard}`.includes(search.value),
		);
	},
});

const fetchClassroomsData = async () => {
	classroomsDataRaw.value = await getClassrooms();
};
onMounted(fetchClassroomsData);
</script>


<style>
.custom-img {
  aspect-ratio: 16/9; /* Enforce the aspect ratio */
  object-fit: cover;    /* Ensures the image covers the aspect ratio box */
  width: 100%;          /* Full width */
  height: auto;         /* Automatically scales height */
}
</style>
  
