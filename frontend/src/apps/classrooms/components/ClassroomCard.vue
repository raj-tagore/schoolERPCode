<template>
    <v-card v-if="classroom">
        <v-img 
            :src="getClassroomImage()" 
            class="custom-img"
        ></v-img>
        <v-card-title>
            {{ classroom.name }}
        </v-card-title>
        <v-card-subtitle>
            <p class="text-body-2 pb-4">
                <v-chip
                    link
                    :to="{ 
                        name: 'Teacher', 
                        params: { 
                            teacherId: classroom.class_teacher_details?.id 
                        }
                    }"
                >
                Class Teacher: {{ classroom.class_teacher_details?.user_details?.full_name || "Loading..." }}
                </v-chip>
            </p>
        </v-card-subtitle>
    </v-card>
</template>

<script setup>
import { getClassroomImage, getClassroom } from "@/apps/classrooms/api";
import { ref, onMounted } from "vue";

const classroom = ref(null);
const props = defineProps({ classroomId: Number });

onMounted(async () => {
  classroom.value = await getClassroom(props.classroomId);
});
</script>