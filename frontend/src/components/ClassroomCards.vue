<template>
<v-container>
    <v-card class="mb-5">
        <v-card-title class="text-h5">Classes</v-card-title>
        <v-card-text>
            <v-row>
            <v-col 
            v-for="(classroom, index) in classroomsData" 
            :key="index" 
            cols="6" 
            md="3" 
            lg="2" >
                <v-card>
                <v-img 
                    :src="getRandomClassroomImage()" 
                    class="custom-img"
                ></v-img>
                <v-card-title class="text-body-1">{{ classroom.name }}</v-card-title>
                <v-card-subtitle>{{ classroom.class_teacher_details.user.first_name || "Loading..." }}</v-card-subtitle>
                <v-card-actions class="d-flex justify-center">
                    <v-btn :to="{ name: 'Classroom', params: { id: classroom.id }}">Enter Class</v-btn>
                </v-card-actions>
                </v-card>
            </v-col>
            </v-row>
        </v-card-text>
    </v-card>

</v-container>
</template>

<script>

import api from '@/services/api'

export default {
name: 'ClassroomCards',
data() {
    return {
    classroomsData: [],
    images: [
        require('@/assets/classrooms/classroom1.png'),
        require('@/assets/classrooms/classroom2.png'),
        require('@/assets/classrooms/classroom3.png'),
    ],
    };
},
methods: {
    getRandomClassroomImage() {
        const index = Math.floor(Math.random() * this.images.length);
        return this.images[index];
    },
    async getClassroomsData() {
        const response = await api.get('api/allocation/classrooms/all/');
        this.classroomsData = response.data;
    },
},
mounted() {
    this.getClassroomsData();
}
};
</script>

<style>
.custom-img {
  aspect-ratio: 16/9; /* Enforce the aspect ratio */
  object-fit: cover;    /* Ensures the image covers the aspect ratio box */
  width: 100%;          /* Full width */
  height: auto;         /* Automatically scales height */
}
</style>
  