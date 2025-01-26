<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-tabs v-model="tabs">
            <v-tab>Overview</v-tab>
            <v-tab>Settings</v-tab>
          </v-tabs>
        </v-card>
        <v-tabs-window v-model="tabs">
          <v-tabs-window-item>
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
              <v-row>
                <v-col 
                  v-for="(classroom, index) in studentClassrooms" 
                  :key="index" 
                  cols="12" 
                  md="3" 
                  lg="2"
                >
                  <v-card>
                    <v-img 
                      :src="getClassroomImage()" 
                      class="custom-img"
                    ></v-img>
                    <v-card-title class="text-body-1">{{ classroom.name }}</v-card-title>
                    <v-card-subtitle>{{ classroom.class_teacher_details?.user?.full_name || "Loading..." }}</v-card-subtitle>
                    <v-card-actions class="d-flex justify-center">
                      <v-btn :to="{ name: 'Classroom', params: { classroomId: classroom.id }}">Enter Class</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </v-tabs-window-item>
          <v-tabs-window-item>
			<StudentSettingsCard :studentId="student.id"></StudentSettingsCard>
          </v-tabs-window-item>
        </v-tabs-window>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getClassroomImage, getClassrooms } from "@/apps/classrooms/api";
import { getStudent } from "@/apps/users/api";
import StudentSettingsCard from "@/apps/users/components/StudentSettingsCard";

const student = ref({});
const studentClassrooms = ref([]);
const tabs = ref(null);

const props = defineProps({
  studentId: Number,
});

const fetchDetails = async () => {
  student.value = await getStudent(props.studentId);
  studentClassrooms.value = await getClassrooms({ student: props.studentId });
};

onMounted(fetchDetails);
</script>

<style>
.custom-img {
  aspect-ratio: 16/9;
  object-fit: cover;
  width: 100%;
  height: auto;
}
</style>
