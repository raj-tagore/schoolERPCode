<template>
  <v-container>
    <v-row class="ma-2 flex justify-center">
      <v-col lg="6">
        <v-card variant="flat">
          <v-card-title>{{ student?.user?.full_name }}</v-card-title>
          <v-card-text>
            <h4 class="text-subtitle-1 mt-4">Student Details:</h4>
            <v-list lines="2">
              <v-list-item
                :title="student?.user?.username"
                :subtitle="`Student No: ${student?.student_no} | Roll No: ${student?.roll_no}`"
                variant="flat"
                rounded="lg"
              />
            </v-list>

            <h4 class="text-subtitle-1 mt-4">Guardian 1:</h4>
            <v-chip-group>
              <v-chip color="primary">Phone: {{ student?.guardian_1?.phone }}</v-chip>
              <v-chip color="secondary">WhatsApp: {{ student?.guardian_1?.whatsapp }}</v-chip>
            </v-chip-group>

            <h4 class="text-subtitle-1 mt-4">Guardian 2:</h4>
            <v-chip-group>
              <v-chip color="primary">Phone: {{ student?.guardian_2?.phone }}</v-chip>
              <v-chip color="secondary">WhatsApp: {{ student?.guardian_2?.whatsapp }}</v-chip>
            </v-chip-group>
          </v-card-text>
        </v-card>
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

const student = ref({});

const props = defineProps({
	studentId: Number,
});

const fetchDetails = async () => {
	student.value = await getStudent(props.studentId);
};

onMounted(fetchDetails);
</script>
