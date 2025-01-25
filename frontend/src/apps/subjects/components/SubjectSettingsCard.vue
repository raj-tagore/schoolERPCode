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
                <v-btn 
                    @click="updateSubject" 
                    color="primary"
                    :loading="isUpdating"
                    :disabled="isUpdating"
                    :append-icon="isSuccess ? 'mdi-check' : (hasError ? 'mdi-alert' : '')"
                    :color="hasError ? 'error' : 'primary'"
                >
                    {{ isSuccess ? 'Updated' : (hasError ? 'Failed!' : 'Update') }}
                </v-btn>
                <v-alert
                  v-if="errorMessage"
                  type="error"
                  class="mt-2"
                  density="compact"
                >
                  {{ errorMessage }}
                </v-alert>
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
const isUpdating = ref(false);
const isSuccess = ref(false);
const hasError = ref(false);
const errorMessage = ref('');

const teacherInfoFromObj = (item) => ({
  title: `${item.user.full_name}`,
  subtitle: item.identifier,
  value: item.id,
});

const updateSubject = async () => {
  isUpdating.value = true;
  isSuccess.value = false;
  hasError.value = false;
  errorMessage.value = '';
  
  try {
    await api.put(`api/allocation/subjects/${props.subject.id}/`, props.subject);
    isSuccess.value = true;
  } catch (error) {
    console.error('Failed to update subject:', error);
    hasError.value = true;
    errorMessage.value = error.response?.data?.detail || 'Failed to update subject';
  } finally {
    isUpdating.value = false;
  }
};

onMounted(async () => {
  teachers.value = await getTeachers();
});
</script>
  