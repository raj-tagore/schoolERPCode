<template>
    <v-container>   
        <v-card>
            <v-card-item>
                <template v-slot:prepend>
        <v-icon icon="mdi-account-school" size="large" color="primary"></v-icon>
      </template>
      <v-card-title>Students Overview</v-card-title>
    </v-card-item>

    <v-card-text>
      <v-row>
        <v-col cols="6">
          <v-card variant="outlined">
            <v-card-item>
              <div class="text-h4 text-primary text-center">{{ stats.total }}</div>
              <div class="text-subtitle-2 text-center">Total Students</div>
            </v-card-item>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card variant="outlined">
            <v-card-item>
              <div class="text-h4 text-primary text-center">{{ stats.pending_approval }}</div>
              <div class="text-subtitle-2 text-center">Pending Approval</div>
            </v-card-item>
          </v-card>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const stats = ref({});

onMounted(async () => {
  try {
    const response = await axios.get('/api/accounts/students/stats/');
    stats.value = response.data;
  } catch (error) {
    console.error('Error fetching student stats:', error);
  }
});
</script>
