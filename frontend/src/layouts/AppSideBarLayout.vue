<template>
	<Suspense>
		<v-app>
			<v-navigation-drawer
				location="right"
				v-model="rightDrawer"
				color="blue-grey">
				<v-card v-if="currentAppMeta">
					<v-card-title>{{ currentAppMeta.displayName }}</v-card-title>
					<v-card-text>
						<v-btn :to="{name: 'All Apps'}">
							Go to All Apps
						</v-btn>
					</v-card-text>
				</v-card>
				<RecursiveList v-for="item in currentAppMeta.menu" :item="item" />
				<span v-if="currentRouteMeta">
					<v-card v-if="currentRouteMeta.displayName">
						<v-card-title>{{ currentRouteMeta.displayName }}</v-card-title>
					</v-card>
					<RecursiveList v-for="item in currentRouteMeta.menu" :item="item" />
				</span>
			</v-navigation-drawer>
				<v-fab 
				app
					absolute
					location="right top"
					@click="rightDrawer = !rightDrawer"
					icon>
					<v-icon>{{ rightDrawer ? 'mdi-close' : 'mdi-menu' }}</v-icon>
				</v-fab>
			<v-main>
				<router-view></router-view>
			</v-main>
		</v-app>
		<template #fallback>
			Loading...
		</template>
	</Suspense>
</template>

<style>
</style>
<script setup>
import { ref, watch, onMounted } from "vue";
import { useDisplay } from "vuetify/lib/framework.mjs";

import { useRoute } from "vue-router";

import RecursiveList from "@/components/RecursiveList.vue";

const currentRoute = useRoute();

const currentRouteMeta = ref(null);

const { mobile } = useDisplay();
const rightDrawer = ref(mobile.value);

const currentAppMeta = ref({});

const getCurrentAppMeta = async () => {
	const route = currentRoute.matched
		.filter(
			(route) => route.path.includes("app") && route?.meta?.getDisplayName,
		)
		?.at(0);

	if (route?.meta) {
		const meta = route.meta;
		meta.menu = await route.meta.getMenu(currentRoute.params);
		meta.displayName = await route.meta.getDisplayName(currentRoute.params);
		return meta;
	}
};

const getRouteMeta = async (route) => {
	const r = route.matched
		.filter((route) => route?.meta?.getMenu && route?.meta?.getDisplayName)
		.pop();

	if (r?.meta) {
		const meta = r.meta;
		meta.menu = await r.meta.getMenu(route.params);
		meta.displayName = await r.meta.getDisplayName(route.params);
		return meta;
	}
};

watch(currentRoute, (route) => {
	getCurrentAppMeta().then((r) => {
		currentAppMeta.value = r;
		console.log("currentAppMeta", currentRouteMeta.value);
	});

	console.log("route", route);

	getRouteMeta(route).then((r) => {
		if (r?.getDisplayName !== currentAppMeta?.value?.getDisplayName) {
			currentRouteMeta.value = r;
		} else {
			currentRouteMeta.value = null;
		}
		console.log("currentRouteMeta", currentRouteMeta.value);
	});
});

onMounted(() => {
	getCurrentAppMeta().then((r) => {
		currentAppMeta.value = r;
	});
		console.log("currentRoute", currentRoute);
		console.log("currentRouteMeta", currentRouteMeta);

	getRouteMeta(currentRoute).then((r) => {
		if (r?.getDisplayName !== currentAppMeta?.value?.getDisplayName) {
			currentRouteMeta.value = r;
		} else {
			currentRouteMeta.value = null;
		}
		console.log("currentRoute", currentRoute);
		console.log("currentRouteMeta", currentRouteMeta);
	});
});
</script>

