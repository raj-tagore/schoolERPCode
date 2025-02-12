<template>
    <v-container>
        <v-card>
            <v-card-title>
                Assignments for {{ subject?.name }} ({{ subject?.classroom_details?.name }})
            </v-card-title>
            <v-card-text>
                <AssignmentsLookup
                    :initialFilters="{ subject: Number(subjectId) }"
                    :initialFiltersInfo="[
                        {
                            key: 'subject',
                            type: 'subject',
                            label: 'Subject',
                            disabled: true
                        }
                    ]"
                />
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script setup>
import AssignmentsLookup from '@/apps/assignments/components/AssignmentsLookup.vue';
import { getSubject } from '@/apps/subjects/api';
import { ref, onMounted } from 'vue';

const props = defineProps({
    subjectId: {
        type: String,
        required: true
    }
});

const subject = ref(null);

onMounted(async () => {
    subject.value = await getSubject(props.subjectId);
});
</script>
