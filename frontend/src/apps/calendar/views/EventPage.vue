<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row class="ma-2 flex justify-center">
          <v-col lg="8">
            <v-card variant="flat">
              <v-card-title>{{ event?.title }}</v-card-title>
              <v-card-text>{{ event?.description }}</v-card-text>
              <v-card-actions>
                <v-btn 
                  to="#"
                  variant="outlined"
                  prepend-icon="mdi-pencil"
                >Edit</v-btn>
                <v-btn 
                  variant="outlined" 
                  prepend-icon="mdi-delete" 
                  color="error"
                >Delete</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col lg="4">
            <v-card variant="flat">
              <v-card-text>
                <h4 class="text-subtitle-1">Created by:</h4>
                <v-list lines="2">
                  <v-list-item 
                    :title="event?.created_by_details?.user_details?.full_name"
                    :subtitle="event?.created_by_details?.user_details?.email"
                    variant="flat"
                    rounded="lg"
                    :to="'#'"
                  />
                </v-list>

                <h4 class="text-subtitle-1 mt-4">Event Time:</h4>
                <v-chip color="primary">Start: {{ formatDate(event?.start) }}</v-chip>
                <v-chip color="red">End: {{ formatDate(event?.end) }}</v-chip>

                <h4 class="text-subtitle-1 mt-4">Assigned to:</h4>
                <div v-if="event?.is_school_wide">
                  <v-chip color="success">The whole school</v-chip>
                </div>
                <div v-else>
                  <div v-if="event?.classrooms?.length > 0">
                    <h5 class="text-subtitle-2 mt-2">Classrooms:</h5>
                    <v-chip-group column>
                      <v-chip
                        v-for="classroom in classroomDetails"
                        :key="classroom.id"
                        color="primary"
                        variant="outlined"
                        :to="{ name: 'Classroom', params: { classroomId: classroom.id }}"
                        link
                      >
                        {{ classroom.name }}
                      </v-chip>
                    </v-chip-group>
                  </div>
                  <div v-if="event?.subjects?.length > 0">
                    <h5 class="text-subtitle-2 mt-2">Subjects:</h5>
                    <v-chip-group column>
                      <v-chip
                        v-for="subject in subjectDetails"
                        :key="subject.id"
                        color="secondary"
                        variant="outlined"
                        :to="{ name: 'Subject', params: { subjectId: subject.id }}"
                        link
                      >
                        {{ subject.name }} ({{ subject.classroom_details?.name }})
                      </v-chip>
                    </v-chip-group>
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getEvent } from "../api";
import { getClassroom } from "@/apps/classrooms/api";
import { getSubject } from "@/apps/subjects/api";

const event = ref({});
const classroomDetails = ref([]);
const subjectDetails = ref([]);

const props = defineProps({
  eventId: Number,
});

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

const fetchDetails = async () => {
  event.value = await getEvent(props.eventId);

  // Fetch classroom details
  if (event.value.classrooms?.length > 0) {
    classroomDetails.value = await Promise.all(
      event.value.classrooms.map((id) => getClassroom(id))
    );
  }

  // Fetch subject details
  if (event.value.subjects?.length > 0) {
    subjectDetails.value = await Promise.all(
      event.value.subjects.map((id) => getSubject(id))
    );
  }
};

onMounted(fetchDetails);
</script>
