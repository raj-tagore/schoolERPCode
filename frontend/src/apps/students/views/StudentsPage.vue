<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row>
          <v-col cols="12" md="4">
            <StudentsStatsCard />
          </v-col>
          <v-col cols="12" md="4">
            <StudentsLookup />
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import StudentsLookup from "@/apps/students/components/StudentsLookup.vue";
import StudentsStatsCard from "@/apps/students/components/StudentsStatsCard.vue";
</script>
