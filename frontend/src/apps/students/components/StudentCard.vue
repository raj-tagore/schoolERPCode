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
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: 'StudentCard',
  props: {
    student: {
      type: Object,
      required: true
    }
  }
}
</script>
