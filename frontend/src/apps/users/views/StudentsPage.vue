<template>
  <v-container>
    <v-row>
        <v-col>
			<v-card>
			  <v-tabs v-model="tabs">
				<v-tab>Overview</v-tab>
				<v-tab>Settings</v-tab>
			  </v-tabs>
			</v-card>
			<v-tabs-window v-model="tabs">
			  <v-tabs-window-item>
				<StudentsLookup />
              </v-tabs-window-item>
			  <v-tabs-window-item>

              </v-tabs-window-item>
            </v-tabs-window>
        </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import StudentsLookup from "@/apps/users/components/StudentsLookup.vue";
import { ref } from "vue";

const tabs = ref(null);
</script>
