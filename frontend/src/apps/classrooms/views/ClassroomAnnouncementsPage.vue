<template>
    <v-container>
        <v-card>
            <v-card-title>
                Announcements for {{ classroom?.name }}
            </v-card-title>
            <v-card-text>
                <AnnouncementsLookup
                    :initialFilters="{ classroom: Number(classroomId) }"
                    :initialFiltersInfo="[
                        {
                            key: 'classroom',
                            type: 'classroom',
                            label: 'Classroom',
                            disabled: true
                        }
                    ]"
                />
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script setup>
import AnnouncementsLookup from '@/apps/announcements/components/AnnouncementsLookup.vue';
import { getClassroom } from '@/apps/classrooms/api';
import { ref, onMounted } from 'vue';

const props = defineProps({
  classroomId: {
    type: String,
    required: true
  }
});

const classroom = ref(null);

onMounted(async () => {
  classroom.value = await getClassroom(props.classroomId);
});
</script>
