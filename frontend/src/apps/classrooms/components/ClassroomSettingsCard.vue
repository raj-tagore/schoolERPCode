<template>
  <v-container>
    <FormCard 
      title="Classroom Settings"
      :onSubmit="handleUpdate"
    >
      <v-row v-if="classroom">
        <v-col>
          <v-text-field 
            label="Standard" 
            v-model="classroom.standard"
            :rules="[v => !!v || 'Standard is required']"
            required
          ></v-text-field>
          <v-text-field 
            label="Name" 
            v-model="classroom.name"
            :rules="[v => !!v || 'Name is required']"
            required
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row v-if="classroom">
        <v-col>
          <v-autocomplete 
            v-if="teachers.length > 0"
            label="Class Teacher" 
            :item-props="getTeacherInfoFromObj" 
            :items="teachers" 
            v-model="classroom.class_teacher"
          ></v-autocomplete>
        </v-col>
        <v-col>
          <v-checkbox 
            label="Is Active" 
            v-model="classroom.is_active"
          ></v-checkbox>
        </v-col>
      </v-row>
    </FormCard>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getClassroom, updateClassroom } from "@/apps/classrooms/api";
import { getTeachers, getTeacherInfoFromObj } from "@/apps/users/api";
import FormCard from "@/components/FormCard.vue";

const props = defineProps({
  classroomId: {
    type: Number,
    required: true
  }
});

const classroom = ref(null);
const teachers = ref([]);

const handleUpdate = async () => {
  try {
    await updateClassroom(classroom.value);
    return { success: true };
  } catch (error) {
    console.error('Failed to update classroom:', error);
    return { success: false, error };
  }
};

onMounted(async () => {
  classroom.value = await getClassroom(props.classroomId);
  teachers.value = await getTeachers();
});
</script>
  