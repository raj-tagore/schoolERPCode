<template>
    <v-card>
        <v-text-field
        v-model="searchQuery"
        label="Click here to search"
        @input="fetchAccounts"
        outlined
        density="comfortable"
        ></v-text-field>
        <v-data-table
            :headers="headers"
            :items="results"
            class="elevation-1"
        >
        <template #item.actions="{ item }">
          <v-btn @click="viewAccount(item)">View</v-btn>
        </template>
        </v-data-table>
    </v-card>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import api from "@/services/api"
  
  const searchQuery = ref("");
  const results = ref([]);
  const headers = ref([
    { title: "Name", value: "user.full_name" },
    { title: "Type", value: "type" },
    { title: "Actions", value: "actions", sortable: false },
  ]);
  
  const fetchAccounts = async () => {
    if (!searchQuery.value) {
      results.value = [];
      return;
    }
  
    const endpoints = [
      { url: "/api/accounts/students/all", type: "Student" },
      { url: "/api/accounts/teachers/all", type: "Teacher" },
      { url: "/api/accounts/parents/all", type: "Parent" },
    ];
  
    try {
      results.value = []; // Clear existing results
      const requests = endpoints.map(async (endpoint) => {
        const response = await api.get(endpoint.url, {
          params: { name: searchQuery.value },
        });
        return response.data.map((account) => ({
          ...account,
          type: endpoint.type,
        }));
      });
  
      const resolvedResults = await Promise.all(requests);
      results.value = resolvedResults.flat();
    } catch (error) {
      console.error("Error fetching accounts:", error);
    }
  };
  </script>
  