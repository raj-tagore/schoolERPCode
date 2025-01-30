<template>
	<v-app>
		<v-navigation-drawer app v-model="leftDrawer"
			color="grey lighten-4">
			<v-list dense>
				<v-list-item>
					<v-card class="ma-2" 
						:title="user.first_name + ' ' + user.last_name"
						:subtitle="user.account?.type || 'No linked account'">
						<template v-slot:append>
							<v-btn icon="mdi-logout" @click="logoutHandler" size="small" variant="text"/>
						</template>
					</v-card>
				</v-list-item>

				<v-divider :thickness="10" class="border-opacity-100"></v-divider>

				<v-list-item :to="{name: 'All Apps'}">
					<v-list-item-title>All Apps</v-list-item-title>
				</v-list-item>

				<v-divider :thickness="10" class="border-opacity-100"></v-divider>

				<RecursiveList v-for="item in appsMenu" :item="item" />

			</v-list>
		</v-navigation-drawer>
		<v-app-bar app color="primary" dark>
			<v-app-bar-nav-icon @click.stop="leftDrawer = !leftDrawer"></v-app-bar-nav-icon>
			<v-toolbar-title>School ERP Dashboard</v-toolbar-title>
		</v-app-bar>
		<v-navigation-drawer app v-if="currentRouteMenu" 
			location="right"
			v-model="rightDrawer"
			color="grey lighten-4">

			<RecursiveList v-for="item in currentRouteMenu" :item="item" />
		</v-navigation-drawer>
		<span v-if="currentRouteMenu">
		<v-fab 
			:v-if="mobile"
			class="position-fixed"
			absolute
			app
			location="right bottom"
			@click="rightDrawer = !rightDrawer"
			icon>
			<v-icon>{{ rightDrawer ? 'mdi-close' : 'mdi-settings' }}</v-icon>
		</v-fab>
		</span>
		<v-app-bar v-if="breadcrumbItems" app color="grey" density="compact">
			<v-breadcrumbs :items="breadcrumbItems">
				<template v-slot:title="{item}">
					<v-btn size="small" :to="item.to">
						{{item.title}}
					</v-btn>
				</template>
			</v-breadcrumbs>
		</v-app-bar>
		<Suspense>
			<v-main>
				<router-view></router-view>

				<template #fallback>
					Loading...
				</template>
			</v-main>
		</Suspense>
	</v-app>
</template>

<style>
</style>
<script setup>
import { ref, watch, onMounted, computed } from "vue";
import { useAuthStore } from "@/stores/auth"; // Pinia store
import { useDisplay } from "vuetify/lib/framework.mjs";

import { useRoute, useRouter } from "vue-router";

import RecursiveList from "@/components/RecursiveList.vue";

import appRoutes from "@/router/app";

const currentRoute = useRoute();

const breadcrumbItems = ref([]);

const currentRouteMenu = ref(null);

const { mdAndUp, smAndDown, mobile } = useDisplay();
const leftDrawer = ref(mdAndUp.value);
const rightDrawer = ref(mdAndUp.value);
const router = useRouter();
const authStore = useAuthStore();

const user = computed(() => authStore.user);

function logoutHandler() {
	router.push({ name: "Login" });
	authStore.logout();
}

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
};

const getRouteMetaRecursive = async (route) =>
	route
		? await Promise.all(
				route
					.filter((route) => route?.meta?.getDisplayName && !route?.props)
					.map(async (route) => ({
						title: await route.meta.getDisplayName(),
						to: { name: route.meta.defaultRoute },
						children: await getRouteMetaRecursive(route?.children),
					})),
			)
		: null;

const appsMenu = ref();

getRouteMetaRecursive(appRoutes).then((menu) => {
	appsMenu.value = menu;
});

const getRoutesMenu = (route) =>
	route.matched
		.filter((route) => route.meta.getMenu)
		.map((route) => route.meta.getMenu(currentRoute.params))
		.pop();

watch(currentRoute, (route) => {
	updateBreadcrumbs(route);
	currentRouteMenu.value = getRoutesMenu(route);
	console.log(currentRouteMenu.value);
});

onMounted(() => {
	updateBreadcrumbs(currentRoute);
	currentRouteMenu.value = getRoutesMenu(currentRoute);
	console.log(currentRouteMenu.value);
});
</script>

