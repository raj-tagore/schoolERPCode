<template>
      <v-container>
        <v-tabs v-model="activeTab" mandatory>
          <v-tab value="dashboard">Dashboard</v-tab>
          <v-tab value="profile">Profile</v-tab>
          <v-tab value="settings">Settings</v-tab>
        </v-tabs>

        <v-tabs-items v-model="activeTab">
          <v-tab-item value="dashboard">
            <p>Welcome to the Dashboard!</p>
          </v-tab-item>
          <v-tab-item value="profile">
            <p>Here is your Profile information.</p>
          </v-tab-item>
          <v-tab-item value="settings">
            <p>Adjust your Settings here.</p>
          </v-tab-item>
        </v-tabs-items>
      </v-container>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('dashboard')
</script>
