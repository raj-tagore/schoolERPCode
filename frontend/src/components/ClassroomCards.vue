<template>
<v-container>
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
        <v-card-title>{{ classroom.name }}</v-card-title>
        <v-card-subtitle class="pb-5">{{ classroom.class_teacher_name || "Loading..." }}</v-card-subtitle>
        </v-card>
    </v-col>
    </v-row>
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

        this.classroomsData.forEach(async (classroom)=> {
            const teacherResponse = await api.get(`api/accounts/all/?id=${classroom.class_teacher}`);
            classroom.class_teacher_name = teacherResponse.data[0].first_name + " " + teacherResponse.data[0].last_name
        })
    },
    async getTeacherName(id) {
        const response = await api.get(`api/accounts/all/?id=${id}`);
        return response.data.first_name + " " + response.data.last_name;
    }
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
  