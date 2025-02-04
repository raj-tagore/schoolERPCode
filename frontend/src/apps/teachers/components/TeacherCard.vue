<template>
  <v-card class="pa-4" variant="flat">
    <v-row>
      <v-col cols="auto">
        <v-avatar size="120" color="grey-lighten-2">
          <v-icon size="64">mdi-account-tie</v-icon>
        </v-avatar>
      </v-col>
      
      <v-col>
        <v-card-title class="text-h5 pa-0 mb-4">
          {{ teacher.user_details.full_name }}
        </v-card-title>
        
        <v-card-text class="pa-0">
          <v-list density="compact">
            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-identifier</v-icon>
              </template>
              <v-list-item-title>Teacher ID: {{ teacher.identifier }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-phone</v-icon>
              </template>
              <v-list-item-title>Phone: {{ teacher.phone }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-whatsapp</v-icon>
              </template>
              <v-list-item-title>WhatsApp: {{ teacher.whatsapp }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-email</v-icon>
              </template>
              <v-list-item-title>{{ teacher.user_details.email }}</v-list-item-title>
            </v-list-item>
          </v-list>

          <div class="mt-4">
            <v-chip
              :color="teacher.user_details.is_approved ? 'success' : 'warning'"
              class="mr-2"
            >
              {{ teacher.user_details.is_approved ? 'Approved' : 'Pending Approval' }}
            </v-chip>
            <v-chip
              :color="teacher.user_details.is_active ? 'success' : 'error'"
            >
              {{ teacher.user_details.is_active ? 'Active' : 'Inactive' }}
            </v-chip>
          </div>
        </v-card-text>
        
        <v-card-actions>
          <v-btn
            v-if="!teacher.user_details.is_approved"
            color="warning"
            :to="{ name: 'EditTeacher', params: { teacherId: teacher.id }}"
            prepend-icon="mdi-check-circle"
            variant="outlined"
          >
            Approve Teacher
          </v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup>
const props = defineProps({
  teacher: {
    type: Object,
    required: true
  }
});
</script>
