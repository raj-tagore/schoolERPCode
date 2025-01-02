<template>
    <v-container>
    <v-card class="pa-4">
        <v-card-title>Student List</v-card-title>
        <v-card-subtitle class="mb-4">Class or Subject information here</v-card-subtitle>
        <v-list v-if="studentsData.length">
            <v-list-item v-for="(student, index) in studentsData"
            :key="index"
            :title="student.first_name + ' ' + student.last_name"
            :subtitle="student.username"
            class="border rounded mb-2 pa-3">
            </v-list-item>
        </v-list>
    </v-card>
    </v-container>
</template>

<script>

import api from '@/services/api'

export default {
name: 'StudentsList',
data() {
    return {
    studentsData: [],
    };
},
methods: {
    async getStudentsData() {
        const response = await api.get('api/users/all/?group=3');
        this.studentsData = response.data;
    },
},
mounted() {
    this.getStudentsData();
}
};
</script>