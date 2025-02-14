<template>
  <v-card class="pa-4" variant="flat">
    <v-row>
      <v-col cols="auto">
        <v-avatar size="120" color="grey-lighten-2">
          <v-icon size="64">mdi-account-circle</v-icon>
        </v-avatar>
      </v-col>
      
      <v-col>
        <div class="d-flex justify-space-between align-center mb-4">
          <v-card-title class="text-h5 pa-0">
            {{ parent.user_details.full_name }}
          </v-card-title>
          
          <v-btn
            v-if="!parent.user_details.is_approved"
            color="warning"
            :to="{ name: 'EditParent', params: { parentId: parent.id }}"
            prepend-icon="mdi-check-circle"
            variant="outlined"
          >
            Approve Parent
          </v-btn>
        </div>
        
        <v-card-text class="pa-0">
          <v-list density="compact">
            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-identifier</v-icon>
              </template>
              <v-list-item-title>Parent ID: {{ parent.identifier }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-phone</v-icon>
              </template>
              <v-list-item-title>Phone: {{ parent.phone }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-whatsapp</v-icon>
              </template>
              <v-list-item-title>WhatsApp: {{ parent.whatsapp }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-email</v-icon>
              </template>
              <v-list-item-title>{{ parent.user_details.email }}</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <template v-slot:prepend>
                <v-icon>mdi-account</v-icon>
              </template>
              <v-list-item-title>{{ parent.user_details.username }}</v-list-item-title>
            </v-list-item>
          </v-list>

          <div class="mt-4">
            <v-chip
              :color="parent.user_details.is_approved ? 'success' : 'warning'"
              class="mr-2"
            >
              {{ parent.user_details.is_approved ? 'Approved' : 'Pending Approval' }}
            </v-chip>
            <v-chip
              :color="parent.user_details.is_active ? 'success' : 'error'"
            >
              {{ parent.user_details.is_active ? 'Active' : 'Inactive' }}
            </v-chip>
          </div>

          <h4 class="text-subtitle-1 mt-4">Children:</h4>
          <v-list lines="2">
            <v-list-item 
              v-for="child in parent.children"
              :key="child.id"
              :title="child.user_details.full_name"
              :subtitle="`Student No: ${child.student_no}`"
              variant="tonal"
              rounded="lg"
              class="ma-2"
              :to="{ name: 'Student', params: { studentId: child.id } }"
            >
              <template v-slot:prepend>
                <v-icon>mdi-school</v-icon>
              </template>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup>
const props = defineProps({
  parent: {
    type: Object,
    required: true
  }
});
</script>
