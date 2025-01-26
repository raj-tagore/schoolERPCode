<template>
    <v-card variant="flat">
        <v-card-title>
            <!-- Search filters -->
            <v-row>
                <v-col cols="12" md="4" lg="3">
                    <v-text-field
                        v-model="filters.name"
                        label="Search by name"
                        density="comfortable"
                        @input="fetchUsers"
                        hide-details
                    ></v-text-field>
                </v-col>
                <v-col cols="12" md="4" lg="2">
                    <v-select
                        v-model="filters.type"
                        :items="[
                            { title: 'All Users', value: null },
                            { title: 'Teachers', value: 'teacher' },
                            { title: 'Students', value: 'student' },
                            { title: 'Parents', value: 'parent' }
                        ]"
                        label="Filter by type"
                        density="comfortable"
                        @update:model-value="fetchUsers"
                        hide-details
                    ></v-select>
                </v-col>
            </v-row>
        </v-card-title>

        <!-- Mobile view: Cards -->
        <div class="d-md-none">
            <v-card
                v-for="item in users"
                :key="item.id"
                class="ma-2 pa-2"
                variant="outlined"
            >
                <div class="d-flex align-center justify-space-between">
                    <v-card-title class="text-subtitle-1">{{ item.user.full_name }}</v-card-title>
                    <v-btn
                        icon="mdi-arrow-right"
                        size="x-small"
                        variant="outlined"
                        @click="viewAccount(item)"
                    ></v-btn>
                </div>
                <v-card-text>
                    <div class="d-flex flex-column gap-1">
                        <div class="d-flex align-center justify-space-between">
                            <span class="text-caption">ID:</span>
                            <span>{{ item.identifier }}</span>
                        </div>
                    </div>
                </v-card-text>
            </v-card>
        </div>

        <!-- Desktop view: Data Table -->
        <v-data-table
            class="d-none d-md-block"
            :headers="headers"
            :items="users"
            :loading="loading"
        >
            <template #item.actions="{ item }">
                <v-btn
                    icon="mdi-arrow-right"
                    size="x-small"
                    variant="outlined"
                    @click="viewAccount(item)"
                ></v-btn>
            </template>
        </v-data-table>
    </v-card>
</template>

<script setup>
import { ref, watch } from "vue";
import { getTeachers, getStudents, getParents } from "@/apps/users/api";
import { useRouter } from 'vue-router';

const router = useRouter();
const users = ref([]);
const loading = ref(false);

const filters = ref({
    name: "",
    type: null
});

const headers = [
    { title: "Name", key: "user.full_name" },
    { title: "ID", key: "identifier" },
    { title: "", key: "actions", align: 'end', sortable: false },
];

const fetchUsers = async () => {
    loading.value = true;
    try {
        const filter = { name: filters.value.name };
        let results = [];
        
        switch (filters.value.type) {
            case 'teacher':
                results = await getTeachers(filter);
                break;
            case 'student':
                results = await getStudents(filter);
                break;
            case 'parent':
                results = await getParents(filter);
                break;
            default:
                const [teachers, students, parents] = await Promise.all([
                    getTeachers(filter),
                    getStudents(filter),
                    getParents(filter)
                ]);
                results = [...teachers, ...students, ...parents];
        }
        users.value = results;
    } catch (error) {
        console.error("Error fetching users:", error);
    } finally {
        loading.value = false;
    }
};

const viewAccount = (item) => {
    if (filters.value.type === 'student' || 
        (filters.value.type === null && item.student_no)) {
        router.push({ name: 'Student', params: { studentId: item.id }});
    }
    // TODO: Add routing for teachers and parents when those routes are created
};

watch(() => filters.value, fetchUsers, { deep: true });

// Initial fetch
fetchUsers();
</script>
  