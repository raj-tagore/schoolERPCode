<script>
import { watch } from "vue";

import { useRoute } from "vue-router";

export default {
	name: "AppTopBarLayout",
	data() {
		return {
			breadcrumbItems: null,
		};
	},
	methods: {
		async populateBreadcrumbs(currentRoute) {
			this.breadcrumbItems = await Promise.all(
				currentRoute.matched
					.filter((route) => route.meta.getDisplayName)
					.map(
						async (route) =>
							await route.meta.getDisplayName(currentRoute.params),
					),
			);
		},
	},
	mounted() {
		const currentRoute = useRoute();
		watch(currentRoute, (route) => {
			this.populateBreadcrumbs(route);
		});
	},
};
</script>

<template>
	<v-app>
		<v-app-bar v-if="breadcrumbItems" app color="grey" density="compact">
			<v-toolbar-title class="flex d-flex justify-space-between">
				{{console.log(breadcrumbItems)}}
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
