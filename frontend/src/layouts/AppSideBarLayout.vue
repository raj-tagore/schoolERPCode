<template>
	<Suspense>
		<v-app>
			<v-navigation-drawer
				location="right"
				v-model="rightDrawer"
				color="accent">
				<v-card v-if="parentMeta" class="mb-4 ma-4">
					<v-card-title>{{ parentMeta.displayName }}</v-card-title>
					<v-card-text>
						<v-btn :to="{name: 'All Apps'}">
							Go to All Apps
						</v-btn>
					</v-card-text>
				</v-card>
				<span v-if="parentMeta">
				<RecursiveList v-for="item in parentMeta.menu" :item="item" />
				</span>
				<span v-if="currentMeta">
					<v-card v-if="currentMeta.displayName" class="mb-4 ma-4">
						<v-card-title>{{ currentMeta.displayName }}</v-card-title>
						<v-card-text v-if="!parentMeta">
							<v-btn :to="{name: 'All Apps'}">
								Go to All Apps
							</v-btn>
					</v-card-text>
					</v-card>
					<RecursiveList v-for="item in currentMeta.menu" :item="item" />
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

const currentRoute = useRoute();
const currentMeta = ref(null);

const { mobile } = useDisplay();
const rightDrawer = ref(!mobile.value);

const parentMeta = ref({});

const getRouteMeta = async (route) => {
	const routes = route.matched.filter(
		(route) => route?.meta?.getMenu && route?.meta?.getDisplayName,
	);

	const routeMeta = {};

	const current = routes.pop();
	if (current?.meta) {
		const meta = current.meta;
		meta.menu = await current.meta.getMenu(route.params);
		meta.displayName = await current.meta.getDisplayName(route.params);
		routeMeta.current = meta;
	}

	const parent = routes.pop();

	if (parent?.meta) {
		const meta = parent.meta;
		meta.menu = await parent.meta.getMenu(route.params);
		meta.displayName = await parent.meta.getDisplayName(route.params);
		routeMeta.parent = meta;
	}
	return routeMeta;
};

watch(currentRoute, (route) => {
	getRouteMeta(route).then((r) => {
		currentMeta.value = r.current;
		parentMeta.value = r.parent;
	});
});

onMounted(() => {
	getRouteMeta(currentRoute).then((r) => {
		currentMeta.value = r.current;
		parentMeta.value = r.parent;
	});
});
</script>

