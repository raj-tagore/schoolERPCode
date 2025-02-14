<template>
    <v-card>
        <v-card-title v-if="title">{{ title }}</v-card-title>
        <v-card-subtitle v-if="subtitle">{{ subtitle }}</v-card-subtitle>
        <v-card-text>
            <v-list lines="two" density="default">
                <v-list-item 
                    v-for="(assignment, index) in AssignmentsData.slice(0, 3)" 
                    :key="index"
                    class="ma-1 pa-2 border"
                >
                    <v-list-item-content>
                        <v-list-item-title>{{ assignment?.title || 'Untitled' }}</v-list-item-title>
                        <v-list-item-subtitle class="mb-2">{{ assignment?.description || 'No description available' }}</v-list-item-subtitle>
                        <v-list-item-text>
                            <v-chip 
                                size="small" 
                                :color="assignment?.subject_details?.classroom_details ? 'secondary' : 'grey'"
                                class="mr-2"
                            >
                                {{ assignment?.subject_details?.name || 'No subject' }}
                                ({{ assignment?.subject_details?.classroom_details?.name || 'No class' }})
                            </v-chip>
                            <v-chip 
                                size="small" 
                                :color="isOverdue(assignment?.due_at) ? 'error' : 'success'"
                            >
                                Due: {{ formatDate(assignment?.due_at) }}
                            </v-chip>
                        </v-list-item-text>
                    </v-list-item-content>
                    <template v-slot:append>
                        <v-btn 
                            v-if="assignment"
                            icon="mdi-arrow-right"
                            variant="flat"
                            border
                            density="comfortable"
                            :to="{ name: 'Assignment', params: { assignmentId: assignment.id } }"
                        ></v-btn>
                    </template>
                </v-list-item>
            </v-list>
            <div v-if="!AssignmentsData?.length" class="text-center pa-4">
                No assignments available
            </div>
        </v-card-text>
        <v-card-actions class="justify-center">
            <v-btn 
                :to="{ name: to || 'Assignments' }"
                variant="outlined"
                density="comfortable"
            >
                View All
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getAssignments } from "@/apps/assignments/api";

const props = defineProps({
    filter: {
        type: Object,
        default: () => ({}),
    },
    title: String,
    subtitle: String,
    to: String,
});

const AssignmentsData = ref([]);

const formatDate = (dateString) => {
    if (!dateString) return 'No date';
    return new Date(dateString).toLocaleDateString("en-US", {
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    });
};

const isOverdue = (dueDate) => {
    if (!dueDate) return false;
    return new Date(dueDate) < new Date();
};

onMounted(async () => {
    AssignmentsData.value = (await getAssignments(props.filter)).results;
});
</script>
