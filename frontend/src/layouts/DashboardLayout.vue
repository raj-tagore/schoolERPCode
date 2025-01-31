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
import { ref, computed } from "vue";
import { useAuthStore } from "@/stores/auth"; // Pinia store
import { useDisplay } from "vuetify/lib/framework.mjs";

import { useRouter } from "vue-router";

import RecursiveList from "@/components/RecursiveList.vue";

import appRoutes from "@/router/app";


const { mdAndUp } = useDisplay();
const leftDrawer = ref(mdAndUp.value);
const router = useRouter();
const authStore = useAuthStore();

const appsMenu = ref();

const user = computed(() => authStore.user);

function logoutHandler() {
	router.push({ name: "Login" });
	authStore.logout();
}

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


</script>


