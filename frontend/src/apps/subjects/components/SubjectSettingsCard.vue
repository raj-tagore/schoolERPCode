<template>
    <v-card>
      <v-card-title>Subject Settings</v-card-title>
      <v-card-text v-if="subject">
        <v-row>
          <v-col>
            <v-text-field label="Name" v-model="subject.name"></v-text-field>
            <v-textarea label="Description" v-model="subject.description"></v-textarea>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-autocomplete v-if="teachers.length>0" label="Teacher" :item-props="teacherInfoFromObj" :items="teachers" v-model="subject.teacher"></v-autocomplete>
          </v-col>
          <v-col>
            <v-checkbox label="Is Active" v-model="subject.is_active"></v-checkbox>
          </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-btn @click="updateSubject" color="primary">Update</v-btn>
            </v-col>
        </v-row>
      </v-card-text>
    </v-card>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { getTeachers } from '@/apps/users/api';
  import api from "@/services/api";
  
  const props = defineProps(['subject']);
  const teachers = ref([]);
  const teacherInfoFromObj = (item) => ({
    title: `${item.user.full_name}`,
    subtitle: item.identifier,
    value: item.id,
  });
  
  const updateSubject = async () => {
    await api.put(`api/allocation/subjects/${props.subject.id}/`, props.subject);
  };
  
  onMounted(async () => {
    teachers.value = await getTeachers();
  });
  </script>
  