<template>
	<Suspense>
		<v-app>
			<v-navigation-drawer
				location="right"
				v-model="rightDrawer"
				color="accent">
				<v-card v-if="routeMeta.app" class="mb-4 ma-4">
					<v-card-title>{{ routeMeta.app.displayName }}</v-card-title>
					<v-card-text>
						<v-btn :to="{name: 'All Apps'}">
							Go to All Apps
						</v-btn>
					</v-card-text>
				</v-card>
				<span v-if="routeMeta.app">
				<RecursiveList v-for="item in routeMeta.app.menu" :item="item" />
				</span>
				<span v-if="routeMeta.current">
					<v-card v-if="routeMeta.current.displayName" class="mb-4 ma-4">
						<v-card-title>{{ routeMeta.current.displayName }}</v-card-title>
					</v-card>
					<RecursiveList v-for="item in routeMeta.current.menu" :item="item" />
				</span>
			</v-navigation-drawer>
				<v-fab 
				app
					location="right top"
					@click="rightDrawer = !rightDrawer"
					icon>
					<v-icon>{{ rightDrawer ? 'mdi-close' : 'mdi-menu' }}</v-icon>
				</v-fab>
			<v-main>
				<slot>
					<router-view></router-view>
				</slot>
			</v-main>
		</v-app>
		<template #fallback>
			Loading...
		</template>
	</Suspense>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useDisplay } from "vuetify/lib/framework.mjs";
import { useRoute } from "vue-router";
import RecursiveList from "@/components/RecursiveList.vue";
import { currentRouteMeta } from "@/router/menu";

const currentRoute = useRoute();

const { mobile } = useDisplay();
const rightDrawer = ref(!mobile.value);
const routeMeta = ref({});

watch(currentRoute, (route) => {
	currentRouteMeta(route).then((r) => {
		routeMeta.value = r;
	});
});

onMounted(() => {
	currentRouteMeta(currentRoute).then((r) => {
		routeMeta.value = r;
	});
});
</script>

