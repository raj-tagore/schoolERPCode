<template>
    <v-card>
      <v-card-title>Class Settings</v-card-title>
      <v-card-text v-if="classroom">
        <v-row>
          <v-col>
            <v-text-field label="Standard" v-model="classroom.standard"></v-text-field>
            <v-text-field label="Name" v-model="classroom.name"></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-autocomplete 
              label="Class Teacher" 
              :item-props="teacherInfoFromObj" 
              :items="teachers" 
              v-model="classroom.class_teacher"
            ></v-autocomplete>
          </v-col>
          <v-col>
            <v-checkbox label="Is Active" v-model="classroom.is_active"></v-checkbox>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn
              @click="updateClassroomHandler(classroom)"
              color="primary"
              :loading="isUpdating"
              :disabled="isUpdating"
              :append-icon="isSuccess ? 'mdi-check' : ''"
            >
              {{ isSuccess ? 'Updated!' : 'Update' }}
            </v-btn>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-text v-else>
        Loading classroom data...
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { getClassroom, updateClassroom } from "@/apps/classrooms/api";
  
  const props = defineProps({
    classroomId: Number, 
  });
  
  const classroom = ref(null);
  const teachers = ref([]); 
  const isUpdating = ref(false);
  const isSuccess = ref(false);
  
  const updateClassroomHandler = async (classroom) => {
    isUpdating.value = true;
    isSuccess.value = false;
    
    try {
      await updateClassroom(classroom);
      isSuccess.value = true;
    } catch (error) {
      console.error('Failed to update classroom:', error);
    } finally {
      isUpdating.value = false;
    }
  };
  
  onMounted(async () => {
    classroom.value = await getClassroom(props.classroomId)
  });
  </script>
  