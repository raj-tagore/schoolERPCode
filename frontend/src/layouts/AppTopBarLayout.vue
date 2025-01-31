<template>
	<Suspense>
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

					<v-divider :thickness="10" class="border-opacity-100"></v-divider>

					<RecursiveList v-for="item in appsMenu" :item="item" />

				</v-list>
			</v-navigation-drawer>
			<v-app-bar app color="primary" dark>
				<v-app-bar-nav-icon @click.stop="leftDrawer = !leftDrawer"></v-app-bar-nav-icon>
				<v-toolbar-title>School ERP Dashboard</v-toolbar-title>
			</v-app-bar>
			<v-navigation-drawer app v-if="currentAppMeta" 
				location="right"
				v-model="rightDrawer"
				color="grey lighten-4">
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
			<span v-if="currentAppMeta">
				<v-fab 
					:v-if="mobile"
					class="position-fixed"
					absolute
					app
					location="right top"
					@click="rightDrawer = !rightDrawer"
					icon>
					<v-icon>{{ rightDrawer ? 'mdi-close' : 'mdi-menu' }}</v-icon>
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
import { ref, watch, onMounted, computed } from "vue";
import { useAuthStore } from "@/stores/auth"; // Pinia store
import { useDisplay } from "vuetify/lib/framework.mjs";

import { useRoute, useRouter } from "vue-router";

import RecursiveList from "@/components/RecursiveList.vue";

import appRoutes from "@/router/app";

const currentRoute = useRoute();

const breadcrumbItems = ref([]);

const currentRouteMeta = ref(null);

const { mdAndUp, smAndDown, mobile } = useDisplay();
const leftDrawer = ref(mdAndUp.value);
const rightDrawer = ref(mdAndUp.value);
const router = useRouter();
const authStore = useAuthStore();

const currentAppMeta = ref({});

const appsMenu = ref();

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

getRouteMetaRecursive(appRoutes).then((menu) => {
	appsMenu.value = menu;
});

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
	updateBreadcrumbs(route);

	getCurrentAppMeta().then((r) => {
		currentAppMeta.value = r;
	});

	getRouteMeta(route).then((r) => {
		if (r?.getDisplayName !== currentAppMeta?.value?.getDisplayName) {
			currentRouteMeta.value = r;
		} else {
			currentRouteMeta.value = null;
		}
	});

	// We are at top level route so no await
});

onMounted(() => {
	updateBreadcrumbs(currentRoute);

	getCurrentAppMeta().then((r) => {
		currentAppMeta.value = r;
	});

	getRouteMeta(currentRoute).then((r) => {
		if (r?.getDisplayName !== currentAppMeta?.value?.getDisplayName) {
			currentRouteMeta.value = r;
		} else {
			currentRouteMeta.value = null;
		}
	});

	// We are at top level route so no await
});
</script>

