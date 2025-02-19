<template>
    <v-container>
        <v-sheet>
            <v-calendar ref="calendar" v-model="currentDate" :events="formattedEvents" view-mode="month"
                color="primary">
                <template v-slot:event="{ event }">
                    <v-chip :color="event.color" class="ma-1" @click.stop="showEvent(event)">
                        {{ event.title }}
                    </v-chip>
                </template>
            </v-calendar>
        </v-sheet>

        <v-dialog v-model="selectedOpen" max-width="600">
            <v-card v-if="selectedEvent">
                <v-card-title class="text-h5 pb-2">{{ selectedEvent.title }}</v-card-title>
                
                <v-card-text>
                    <EventDialogCard :event="selectedEvent" />
                </v-card-text>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn 
                        color="grey-darken-1" 
                        variant="text" 
                        @click="selectedOpen = false"
                    >
                        Close
                    </v-btn>
                    <v-btn 
                        color="primary" 
                        variant="tonal"
                        :to="{ name: 'Event', params: { eventId: selectedEvent.id } }"
                    >
                        View Details
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { getCalendar } from '@/apps/calendar/api';
import EventDialogCard from '@/apps/calendar/components/EventDialogCard.vue';

// Calendar state
const currentDate = ref(new Date());
const events = ref([]);
const selectedEvent = ref(null);
const selectedOpen = ref(false);

// Replace onMounted and add fetchEvents function
const fetchEvents = async () => {
    try {
        const date = new Date(currentDate.value);
        const filter = {
            month: date.getMonth() + 1, // Months are 0-based in JS
            year: date.getFullYear()
        };
        const response = await getCalendar(filter);
        events.value = response;
    } catch (error) {
        console.error('Error fetching events:', error);
    }
};

// Watch for changes in view mode and current date
watch([currentDate], () => {
    fetchEvents();
});

onMounted(() => {
    fetchEvents();
});

// Format events for the calendar
const formattedEvents = computed(() => {
    return events.value.map(event => ({
        title: event.title,
        start: new Date(event.start),
        end: new Date(event.end),
        color: event.is_school_wide ? 'red' : 'primary',
        allDay: false,
        originalEvent: event,
    }));
});

// Open the event dialog when a chip is clicked
const showEvent = (event) => {
    selectedEvent.value = event.originalEvent;
    selectedOpen.value = true;
};
</script>