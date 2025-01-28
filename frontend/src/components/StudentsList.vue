<template>
    <v-container>
    <v-card class="pa-4">
        <v-card-title>Student List</v-card-title>
        <v-card-subtitle class="mb-4">Class or Subject information here</v-card-subtitle>
        <v-list v-if="studentsData.length">
            <v-list-item v-for="(student, index) in studentsData"
            :key="index"
            :title="student.user.first_name + ' ' + student.user.last_name"
            :subtitle="student.user.username"
            class="border rounded mb-2 pa-3">
            </v-list-item>
        </v-list>
    </v-card>
    </v-container>
</template>

<script>

import { ref, onMounted } from 'vue';
import { api } from '@/services/api';

export default {
  name: 'StudentsList',
  setup() {
    const studentsData = ref([]);

    const getStudentsData = async () => {
      const response = await api.get('api/accounts/students/all');
      studentsData.value = response.data;
    };

    onMounted(() => {
      getStudentsData();
    });

    return {
      studentsData,
      getStudentsData,
    };
  },
};

</script>
