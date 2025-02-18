<template>
    <v-container>
      <!-- Toolbar for view mode and weekday selection -->
      <v-sheet class="d-flex" height="54" tile>
        <v-select
          v-model="type"
          :items="types"
          class="ma-2"
          density="compact"
          label="View Mode"
          variant="outlined"
          hide-details
        />
        <v-select
          v-model="weekday"
          :items="weekdays"
          class="ma-2"
          density="compact"
          label="Weekdays"
          variant="outlined"
          hide-details
        />
      </v-sheet>
  
      <!-- Calendar -->
      <v-sheet>
        <v-calendar
          ref="calendar"
          v-model="currentDate"
          :events="formattedEvents"
          :view-mode="type"
          :weekdays="weekday"
          :event-color="getEventColor"
          color="primary"
        >
          <!-- Render each event as a clickable chip -->
          <template v-slot:event="{ event }">
            <v-chip
              :color="event.color"
              class="ma-1"
              small
              text-color="white"
              @click.stop="showEvent(event)"
            >
              {{ event.title }}
            </v-chip>
          </template>
        </v-calendar>
      </v-sheet>
  
      <!-- Event Dialog -->
      <v-dialog v-model="selectedOpen" max-width="600">
        <v-card v-if="selectedEvent">
          <v-card-title>{{ selectedEvent.title }}</v-card-title>
          <v-card-text>
            <p>{{ selectedEvent.description }}</p>
            <div class="pa-2 ma-2 border rounded-lg">
                <p class="text-caption">
                Created by: {{ selectedEvent.created_by_details?.user_details?.full_name }}
                </p>
                <p class="text-caption">
                From: {{ new Date(selectedEvent.start).toLocaleString() }}
                </p>
                <p class="text-caption">
                To: {{ new Date(selectedEvent.end).toLocaleString() }}
                </p>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" variant="outlined" @click="selectedOpen = false">
              Close
            </v-btn>
            <v-btn color="primary" variant="outlined">View Event</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue';
  import { getEvents } from '@/apps/calendar/api';
  
  // Calendar state
  const currentDate = ref(new Date());
  const events = ref([]); // Fetched events
  const selectedEvent = ref(null);
  const selectedOpen = ref(false);
  
  // Calendar view options
  const type = ref('month');
  const types = ['month', 'week', 'day'];
  const weekday = ref([0, 1, 2, 3, 4, 5, 6]);
  const weekdays = [
    { title: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
    { title: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
    { title: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
    { title: 'Mon, Wed, Fri', value: [1, 3, 5] },
  ];
  
  // Fetch events when the component mounts
  onMounted(async () => {
    try {
      const response = await getEvents({});
      events.value = response.results;
    } catch (error) {
      console.error('Error fetching events:', error);
    }
  });
  
  // Format events for the calendar
  const formattedEvents = computed(() => {
    return events.value.map(event => ({
      title: event.title,
      start: new Date(event.start),
      end: new Date(event.end),
      color: event.is_school_wide ? 'red' : 'primary',
      allDay: false, // Adjust if your event should be all-day
      originalEvent: event,
    }));
  });
  
  // Determine the color for an event
  const getEventColor = (event) => event.color;
  
  // Open the event dialog when a chip is clicked
  const showEvent = (event) => {
    selectedEvent.value = event.originalEvent;
    selectedOpen.value = true;
  };
  </script>
  