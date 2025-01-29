<script setup>
import { ref, watch, onMounted } from "vue";

import { useRoute } from "vue-router";

const currentRoute = useRoute();

const breadcrumbItems = ref([]);

const updateBreadcrumbs = async (route) => {
	breadcrumbItems.value = (
		await Promise.all(
			route.matched
				.filter((route) => route.meta.getDisplayName)
				.map(async (route) => ({
					title: await route.meta.getDisplayName(currentRoute.params),
					to: {
						name: route.meta.defaultRoute,
						params: currentRoute.params,
					},
				})),
		)
	).slice(-3);
	const breadcrumbsLength = breadcrumbItems.value.length;
	const lastBreadcrumb = breadcrumbItems.value[breadcrumbsLength - 1];
	if (lastBreadcrumb) {
		lastBreadcrumb.active = true;
		lastBreadcrumb.disabled = false;
	}
}

watch(currentRoute, updateBreadcrumbs);

onMounted(() => updateBreadcrumbs(currentRoute))
</script>

<template>
	<v-app>
		<v-app-bar v-if="breadcrumbItems" app color="grey" density="compact">
			<v-breadcrumbs :items="breadcrumbItems">
				<template v-slot:title="{item}">
					<v-btn size="small" :to="item.to">
						{{item.title}}
					</v-btn>
				</template>
			</v-breadcrumbs>
		</v-app-bar>
		<v-main>
			<router-view></router-view>
		</v-main>
	</v-app>
</template>



<style>
</style>
