<template>
	<v-container>
		<v-row>
			<v-col>
				<v-card>
					<v-card-title>All Apps</v-card-title>
					<v-card-text>
						<v-row>
							<v-col lg="4">
								<v-text-field
									v-model="search"
									label="Search by app name"
									density="comfortable"
									@update:model-value="updateFilter"
									clearable
								/>
							</v-col>
						</v-row>
						<v-row>
							<v-col 
								cols="6" 
								md="3" 
								lg="3"
								v-for="app in filteredApps" :key="app.id">
								<v-card :to="{name: app.defaultRoute}">
									<v-card-title>
										<v-icon :icon="app.icon" class="me-2" />
										{{ app.getDisplayName() }}
									</v-card-title>
									<v-card-text>{{ app.description }}</v-card-text>
								</v-card>
							</v-col>
						</v-row>
					</v-card-text>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import { ref, watch } from "vue";

import appRoutes from "@/router/app";

const apps = ref(appRoutes.map((route) => route.meta));

const filteredApps = ref([...apps.value]);

const search = ref("");

watch(search, () => {
	filteredApps.value = apps.value.filter((app) =>
		app.getDisplayName().toLowerCase().includes(search.value.toLowerCase()),
	);
});
</script>
