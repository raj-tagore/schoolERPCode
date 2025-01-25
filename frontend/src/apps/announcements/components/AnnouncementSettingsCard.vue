<template>
  <FormCard 
    title="Announcement Settings"
    :onSubmit="handleUpdate"
  >
    <v-row v-if="announcement">
      <v-col>
        <v-text-field 
          label="Title" 
          v-model="announcement.title"
          :rules="[v => !!v || 'Title is required']"
          required
        ></v-text-field>
        <v-textarea 
          label="Description" 
          v-model="announcement.description"
          :rules="[v => !!v || 'Description is required']"
          required
        ></v-textarea>
      </v-col>
    </v-row>
    <v-row v-if="announcement">
      <v-col>
        <v-select
          label="Priority"
          v-model="announcement.priority"
          :items="['low', 'medium', 'high']"
        ></v-select>
      </v-col>
      <v-col>
        <v-checkbox label="Is Active" v-model="announcement.is_active"></v-checkbox>
        <v-checkbox label="Is School Wide" v-model="announcement.is_school_wide"></v-checkbox>
      </v-col>
    </v-row>
    <v-row v-if="announcement">
      <v-col>
        <v-autocomplete 
          v-if="teachers.length > 0" 
          label="Signed By" 
          :item-props="getTeacherInfoFromObj" 
          :items="teachers" 
          v-model="announcement.signed_by"
        ></v-autocomplete>
      </v-col>
    </v-row>
    <v-row v-if="announcement">
      <v-col>
        <v-text-field
          label="Release Date"
          type="datetime-local"
          v-model="announcement.release_at"
          :value="formatDateForInput(announcement.release_at)"
          @input="announcement.release_at = $event.target.value"
          :rules="[v => !!v || 'Release date is required']"
          required
        ></v-text-field>
      </v-col>
      <v-col>
        <v-text-field
          label="Expiry Date"
          type="datetime-local"
          v-model="announcement.expiry_at"
          :value="formatDateForInput(announcement.expiry_at)"
          @input="announcement.expiry_at = $event.target.value"
          :rules="[v => !!v || 'Expiry date is required']"
          required
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row v-if="announcement">
      <v-col>
        <v-autocomplete 
          v-if="classrooms.length > 0"
          label="Classrooms" 
          :items="classrooms"
          v-model="announcement.classrooms"
          :item-props="getClassroomInfoFromObj"
          multiple
          chips
        ></v-autocomplete>
      </v-col>
      <v-col>
        <v-autocomplete 
          v-if="subjects.length > 0"
          label="Subjects" 
          :items="subjects"
          v-model="announcement.subjects"
          :item-props="getSubjectInfoFromObj"
          multiple
          chips
        ></v-autocomplete>
      </v-col>
    </v-row>
  </FormCard>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getAnnouncement, updateAnnouncement } from "../api";
import { getTeachers, getTeacherInfoFromObj } from '@/apps/users/api';
import { getClassrooms, getClassroomInfoFromObj } from '@/apps/classrooms/api';
import { getSubjects, getSubjectInfoFromObj } from '@/apps/subjects/api';
import FormCard from "@/components/FormCard.vue";

const props = defineProps({
  announcementId: {
    type: Number,
    required: true
  }
});

const announcement = ref(null);
const teachers = ref([]);
const classrooms = ref([]);
const subjects = ref([]);

const formatDateForInput = (dateString) => {
  if (!dateString) return '';
  return new Date(dateString).toISOString().slice(0, 16);
};

const handleUpdate = async () => {
  return await updateAnnouncement(props.announcementId, announcement.value);
};

onMounted(async () => {
  announcement.value = await getAnnouncement(props.announcementId);
  teachers.value = await getTeachers();
  classrooms.value = await getClassrooms();
  subjects.value = await getSubjects();
});
</script>
