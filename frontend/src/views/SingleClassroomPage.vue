<template>
    <v-container fluid>
      <v-row>
        <v-col cols="12" sm="12" md="8">
          <h1>{{ classroom.name }} (Standard {{ classroom.standard }})</h1>
        </v-col>
      </v-row>
      
      <v-row>
        <!-- Classroom Info Card -->
        <v-col cols="12" sm="12" md="6">
          <DataCard title="Classroom Information">
            <template #content>
              <p><strong>ID:</strong> {{ classroom.id }}</p>
              <p><strong>Active:</strong> {{ classroom.is_active }}</p>
              <p><strong>Class Teacher:</strong> {{ getTeacherName(classroom.class_teacher) }}</p>
            </template>
          </DataCard>
        </v-col>
  
        <!-- Subjects Card -->
        <v-col cols="12" sm="12" md="6">
          <DataCard title="Subjects">
            <template #content>
              <ul>
                <li v-for="subject in subjects" :key="subject.id">
                  {{ subject.name }}
                </li>
              </ul>
            </template>
          </DataCard>
        </v-col>
      </v-row>
      
      <v-row>
        <!-- Announcements Card -->
        <v-col cols="12" sm="12" md="6">
          <AnnouncementsCard :announcements="announcements" />
        </v-col>
        
        <!-- Students Card -->
        <v-col cols="12" sm="12" md="6">
          <DataCard title="Students">
            <template #content>
              <ul>
                <li v-for="student in students" :key="student.id">
                  {{ student.username }}
                </li>
              </ul>
            </template>
          </DataCard>
        </v-col>
      </v-row>
      
      <!-- Optionally, you could add another card for Teachers or other details as needed -->
    </v-container>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  import DataCard from '@/components/DataCard.vue'
  import AnnouncementsCard from '@/components/AnnouncementsCard.vue'
  import api from '@/services/api'
  
  const route = useRoute()
  const classroomId = route.params.id
  
  const classroom = ref({})
  const announcements = ref([])
  const students = ref([])
  const subjects = ref([])
  // const teacher = ref([]) // if you want to fetch teachers as well
  
  onMounted(async () => {
    try {
      await fetchClassroom()
      await fetchAnnouncements()
      await fetchStudents()
      await fetchSubjects()
    } catch (error) {
      console.error(error)
    }
  })
  
  async function fetchClassroom() {
    const response = await api.get(`/api/allocation/classrooms/${classroomId}`)
    classroom.value = response.data
  }
  
  async function fetchAnnouncements() {
    const response = await api.get(`/api/announcements/all/?classroom=${classroomId}`)
    announcements.value = response.data
  }
  
  async function fetchStudents() {
    const response = await api.get(`/api/accounts/all/?classroom=${classroomId}`)
    students.value = response.data
  }
  
  async function fetchSubjects() {
    const response = await api.get(`/api/allocation/subjects/all/?classroom=${classroomId}`)
    subjects.value = response.data
  }

  async function getTeacherName(id) {
    const response = await api.get(`/api/accounts/all/?id=${id}`)
    return response.data[0]["first_name"]+response.data[0]["last_name"]
  }
  </script>
  
  <style scoped>
  h1 {
    margin-bottom: 20px;
  }
  </style>
  