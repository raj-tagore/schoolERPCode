<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row class="ma-2 flex justify-center">
          <v-col lg="8">
            <v-card variant="flat">
              <v-card-title>{{ announcement?.title }}</v-card-title>
              <v-card-text>{{ announcement?.description }}</v-card-text>
              <v-card-actions>
                <v-btn :to="{ name: 'EditAnnouncement', params: { announcementId: announcement.id } }"
                variant="outlined"
                prepend-icon="mdi-pencil"
                >Edit</v-btn>
                <v-btn variant="outlined" prepend-icon="mdi-delete" color="error">Delete</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col lg="4">
            <v-card variant="flat">
              <v-card-text>
                <h4 class="text-subtitle-1">Signed by:</h4>
                  <v-list lines="2">
                    <v-list-item 
                      :title="announcement?.signed_by_details?.user_details?.full_name"
                      :subtitle="announcement?.signed_by_details?.user_details?.email"
                      :variant="'flat'"
                      rounded="lg"
                      :to="'#'"
                    />
                  </v-list>
                  <h4 class="text-subtitle-1 mt-4">Dates:</h4>
                  <v-chip color="primary">Release: {{ formatDate(announcement.release_at) }}</v-chip>
                  <v-chip color="red">Expiry: {{ formatDate(announcement.expiry_at) }}</v-chip>

                  <h4 class="text-subtitle-1 mt-4">Assigned to:</h4>
                  <div v-if="announcement?.is_school_wide">
                    <v-chip color="success">The whole school</v-chip>
                  </div>
                  <div v-else>
                    <div v-if="announcement?.classrooms?.length > 0">
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
                    <div v-if="announcement?.subjects?.length > 0">
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
import { getAnnouncement } from "../api";
import { getClassroom } from "@/apps/classrooms/api";
import { getSubject } from "@/apps/subjects/api";

const announcement = ref({});
const classroomDetails = ref([]);
const subjectDetails = ref([]);
const tabs = ref(null);
const props = defineProps({
	announcementId: Number,
});

const formatDate = (dateString) => {
	return new Date(dateString).toLocaleString("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
		hour: "2-digit",
		minute: "2-digit",
		second: "2-digit",
	});
};

const fetchDetails = async () => {
	announcement.value = await getAnnouncement(props.announcementId);

	// Fetch classroom details
	if (announcement.value.classrooms?.length > 0) {
		classroomDetails.value = await Promise.all(
			announcement.value.classrooms.map((id) => getClassroom(id)),
		);
	}

	// Fetch subject details
	if (announcement.value.subjects?.length > 0) {
		subjectDetails.value = await Promise.all(
			announcement.value.subjects.map((id) => getSubject(id)),
		);
	}
};

onMounted(fetchDetails);
</script>
