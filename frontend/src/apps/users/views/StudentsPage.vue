<template>
  <v-container>
    <v-row>
        <v-col>
			<v-card>
			  <v-tabs
				background-color="deep-purple accent-4"
				center-active
				dark
				density="comfortable"
				align-tabs="center"
				v-model="tabs"
			  >
				<v-tab>Overview</v-tab>
				<v-tab>Settings</v-tab>
			  </v-tabs>
			</v-card>
			<v-tabs-window v-model="tabs">
			  <v-tabs-window-item>
                <v-row>
                    <v-col cols="12" md="4">
                        <StudentsStatsCard />
                    </v-col>
                    <v-col cols="12" md="4">
				        <StudentsLookup />
                    </v-col>
                </v-row>
              </v-tabs-window-item>
			  <v-tabs-window-item>
                <StudentsSettingsCard></StudentsSettingsCard>
              </v-tabs-window-item>
            </v-tabs-window>
        </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import StudentsLookup from "@/apps/users/components/StudentsLookup.vue";
import StudentsSettingsCard from "@/apps/users/components/StudentsSettingsCard.vue";
import StudentsStatsCard from "@/apps/users/components/StudentsStatsCard.vue";
import { ref } from "vue";

const tabs = ref(null);
</script>
