<template>
  <v-container>
    <v-row class="ma-2">
      <v-col cols="12">
        <TeacherCard :teacher="teacher" v-if="teacher?.user_details" />
      </v-col>
    </v-row>
    <v-container>
      <h4 class="text-h6 mb-4">Class Teacher for Classrooms</h4>
      <ClassroomsCard :filter="{ class_teacher: props.teacherId }" />
    </v-container>
    <v-container>
      <h4 class="text-h6 mb-4">Teaching Classrooms</h4>
      <ClassroomsCard :filter="{ teacher: props.teacherId }" />
    </v-container>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getTeacher } from "@/apps/teachers/api";
import ClassroomsCard from "@/apps/classrooms/components/ClassroomsCard";
import TeacherCard from "@/apps/teachers/components/TeacherCard";

const teacher = ref({});

const props = defineProps({
  teacherId: Number,
});

const fetchDetails = async () => {
  teacher.value = await getTeacher(props.teacherId);
};

onMounted(fetchDetails);
</script>
