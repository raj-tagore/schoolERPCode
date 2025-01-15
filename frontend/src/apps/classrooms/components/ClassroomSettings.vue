<template>
    <v-card class="ma-4 pa-4">
      <v-card-title>Settings</v-card-title>
      <v-card-text v-if="classroom">
        <v-row>
          <v-col cols="12" lg="6">
            <v-text-field label="Standard" v-model="classroom.standard"></v-text-field>
          </v-col>
          <v-col cols="12" lg="6">
            <v-text-field label="Name" v-model="classroom.name"></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" lg="6">
            <v-autocomplete 
              label="Class Teacher" 
              :item-props="teacherInfoFromObj" 
              :items="teachers" 
              v-model="classroom.class_teacher"
            ></v-autocomplete>
          </v-col>
          <v-col cols="12" lg="6">
            <v-checkbox label="Is Active" v-model="classroom.is_active"></v-checkbox>
          </v-col>
        </v-row>
        <v-row>
          <v-btn @click="updateClassroom" color="primary">Update</v-btn>
        </v-row>
      </v-card-text>
      <v-card-text v-else>
        Loading classroom data...
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { getClassroom, updateClassroom as apiUpdateClassroom } from "@/apps/classrooms/api";
  
  const props = defineProps({
    classroomId: Number, // Accept only classroomId as a prop
  });
  
  const classroom = ref(null);
  const teachers = ref([]); // Fetch or manage teacher data if needed
  
  const fetchClassroom = async () => {
    try {
      classroom.value = await getClassroom(props.classroomId);
    } catch (error) {
      console.error("Failed to fetch classroom:", error);
    }
  };
  
  const updateClassroom = async () => {
    try {
      await apiUpdateClassroom(classroom.value);
      console.log("Classroom updated successfully!");
    } catch (error) {
      console.error("Failed to update classroom:", error);
    }
  };
  
  onMounted(fetchClassroom);
  </script>
  