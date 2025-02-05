<template>
  <v-card class="pa-4" variant="flat">
    <v-row>
      <v-col cols="auto">
        <v-avatar size="120" color="grey-lighten-2">
          <v-icon size="64">mdi-account-circle</v-icon>
        </v-avatar>
      </v-col>
      
      <v-col>
        <v-card-title class="text-h5 pa-0 mb-4">
          {{ student.user_details.full_name }}
        </v-card-title>
        
        <v-card-text class="pa-0">
          <v-list density="compact">
            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-identifier</v-icon>
              </template>
              <v-list-item-title>Student No: {{ student.student_no }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-format-list-numbered</v-icon>
              </template>
              <v-list-item-title>Roll No: {{ student.roll_no }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-email</v-icon>
              </template>
              <v-list-item-title>{{ student.user_details.email }}</v-list-item-title>
            </v-list-item>
          </v-list>

          <div class="mt-4">
            <v-chip
              :color="student.user_details.is_approved ? 'success' : 'warning'"
              class="mr-2"
            >
              {{ student.user_details.is_approved ? 'Approved' : 'Pending Approval' }}
            </v-chip>
            <v-chip
              :color="student.user_details.is_active ? 'success' : 'error'"
            >
              {{ student.user_details.is_active ? 'Active' : 'Inactive' }}
            </v-chip>
          </div>

          <h4 class="text-subtitle-1 mt-4">Guardians:</h4>
          <v-list lines="2">
            <v-list-item 
              v-if="guardian1?.user_details"
              :title="guardian1.user_details.full_name"
              :subtitle="guardian1.user_details.email"
              variant="tonal"
              rounded="lg"
              class="ma-2"
              :to="{ name: 'Parent', params: { parentId: guardian1.id } }"
            >
              <template v-slot:prepend>
                <v-icon>mdi-account-child</v-icon>
              </template>
            </v-list-item>
            
            <v-list-item 
              v-if="guardian2?.user_details"
              :title="guardian2.user_details.full_name"
              :subtitle="guardian2.user_details.email"
              variant="tonal"
              rounded="lg"
              class="ma-2"
              :to="{ name: 'Parent', params: { parentId: guardian2.id } }"
            >
              <template v-slot:prepend>
                <v-icon>mdi-account-child</v-icon>
              </template>
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-card-actions>
            <v-btn
            v-if="!student.user_details.is_approved"
            color="warning"
            :to="{ name: 'EditStudent', params: { studentId: student.id }}"
            prepend-icon="mdi-check-circle"
            variant="outlined"
            >
            Approve Student
          </v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getParent } from '@/apps/parents/api';

const props = defineProps({
  student: {
    type: Object,
    required: true
  }
});

const guardian1 = ref(null);
const guardian2 = ref(null);

const fetchGuardians = async () => {
  if (props.student.guardian_1) {
    guardian1.value = await getParent(props.student.guardian_1);
  }
  if (props.student.guardian_2) {
    guardian2.value = await getParent(props.student.guardian_2);
  }
};

onMounted(fetchGuardians);
</script>
