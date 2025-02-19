<template>
  <div class="pa-4 ma-2 bg-grey-lighten-4 rounded-lg">
    <div class="d-flex align-center mb-4">
      <v-avatar color="primary" class="mr-3">
        <v-icon icon="mdi-account" color="white"></v-icon>
      </v-avatar>
      <div>
        <div class="text-subtitle-1">
          {{ event.created_by_details?.user_details?.full_name }}
        </div>
        <div class="text-caption text-medium-emphasis">
          {{ event.created_by_details?.user_details?.email }}
        </div>
      </div>
    </div>

    <div class="d-flex align-center mb-2">
      <v-icon icon="mdi-clock-start" class="mr-2" color="primary"></v-icon>
      <span>{{ new Date(event.start).toLocaleString() }}</span>
    </div>
    
    <div class="d-flex align-center mb-4">
      <v-icon icon="mdi-clock-end" class="mr-2" color="error"></v-icon>
      <span>{{ new Date(event.end).toLocaleString() }}</span>
    </div>

    <div v-if="event.description" class="mt-4">
      <div class="text-subtitle-2 mb-1">Description</div>
      <div class="text-body-2 text-medium-emphasis">{{ event.description }}</div>
    </div>

    <!-- Scope of Event -->
    <div class="mt-4">
      <div class="text-subtitle-2 mb-2">Event Scope</div>
      <div v-if="event.is_school_wide">
        <v-chip color="success" size="small">School Wide</v-chip>
      </div>
      <div v-else class="d-flex flex-wrap gap-2">
        <v-chip 
          v-if="event.classrooms?.length"
          color="primary" 
          size="small"
        >
          {{ event.classrooms.length }} Classroom(s)
        </v-chip>
        <v-chip 
          v-if="event.subjects?.length"
          color="secondary" 
          size="small"
        >
          {{ event.subjects.length }} Subject(s)
        </v-chip>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  event: {
    type: Object,
    required: true
  }
});
</script>
