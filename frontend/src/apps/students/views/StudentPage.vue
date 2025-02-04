<template>
  <v-container>
    <v-row class="ma-2">
      <v-col cols="12">
        <StudentCard :student="student" v-if="student?.user_details" />
      </v-col>
    </v-row>
    <v-container>
      <h4 class="text-h6 mb-4">Enrolled Classrooms</h4>
      <ClassroomsCard :filter="{ student: props.studentId }" />
    </v-container>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getStudent } from "@/apps/students/api";
import ClassroomsCard from "@/apps/classrooms/components/ClassroomsCard";
import StudentCard from "@/apps/students/components/StudentCard";

const student = ref({});

const props = defineProps({
	studentId: Number,
});

const fetchDetails = async () => {
	student.value = await getStudent(props.studentId);
};

onMounted(fetchDetails);
</script>
