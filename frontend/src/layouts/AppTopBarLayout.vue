<script setup>
import { useRoute } from "vue-router";

const currentRoute = useRoute();

const breadcrumbItems = await Promise.all(
	currentRoute.matched
		.filter((route) => route.meta.getDisplayName)
		.map(async (route) => await route.meta.getDisplayName(currentRoute.params)),
);
console.log(breadcrumbItems);
</script>

<template>
	<v-app>
		<v-app-bar app color="grey" density="compact">
			<v-toolbar-title class="flex d-flex justify-space-between">
				<v-breadcrumbs :items="breadcrumbItems"></v-breadcrumbs>
			</v-toolbar-title>


		</v-app-bar>


		<v-main>
			<router-view></router-view>
		</v-main>
	</v-app>
</template>



<style>
</style>
