<template>
    <v-container>
      <v-row>
        <v-col 
          v-for="classroom in classrooms" 
          :key="classroom.id" 
          cols="12" sm="6" md="4"
        >
          <v-card
            class="ma-2"
            outlined
            @click="goToClassroom(classroom.id)"
            style="cursor: pointer;"
          >
            <v-card-title>{{ classroom.name }}</v-card-title>
            <v-card-text>
              <div><strong>Standard:</strong> {{ classroom.standard }}</div>
              <div><strong>Status:</strong> {{ classroom.is_active ? 'Active' : 'Inactive' }}</div>
              <div><strong>Class Teacher:</strong> {{ classroom.class_teacher }}</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    name: 'ClassroomCards',
    props: {
      classrooms: {
        type: Array,
        required: true,
      },
    },
    methods: {
      goToClassroom(classroomId) {
        // Assuming you have a route named 'SingleClassroom' that takes an 'id' param
        this.$router.push({ name: 'SingleClassroom', params: { id: classroomId } });
      },
    },
  };
  </script>
  