<template>
    <v-container>
        <v-row>
            <v-col lg="4">
                <v-text-field
                    v-model="search"
                    label="Search by classroom name"
                    density="comfortable"
                    @update:model-value="updateFilter"
                    clearable
                />
            </v-col>
        </v-row>
        <ClassroomsCard :filter="filter" />
    </v-container>
</template>

<script setup>
import { ref, reactive } from "vue";
import ClassroomsCard from "@/apps/classrooms/components/ClassroomsCard.vue";

const search = ref("");
const filter = reactive({});

const updateFilter = (value) => {
    if (value) {
        filter.name = value;
    } else {
        delete filter.name;
    }
};
</script>
