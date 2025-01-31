<template>
	<v-data-table-server
		v-if="mobile || forceMobile"
		:items-length="itemsLen"
		:headers="[]"
		:items="items"
		@update:options="fetchData"
		:search="search"
		:loading="loading"
	>
		<template #headers={}></template>
		<template #item={item}>
			<v-card
				class="ma-2 pa-2"
				variant="outlined"
			>
				<div class="d-flex align-center justify-space-between">
					<v-card-title class="text-subtitle-1">{{ item[title.key] }}</v-card-title>
					<v-btn v-if="getToFunction"
						icon="mdi-arrow-right"
						size="small"
						variant="outlined"
						:to="getToFunction(item)"
					></v-btn> 
				</div>
				<v-card-text>
					<div class="d-flex flex-column gap-1">
						<div v-for="header in data_headers" class="d-flex align-center justify-space-between">
							<span class="text-caption">{{header.title}}:</span>
							<span v-if="header.formatFunc">{{ header.formatFunc(item[header.key]) }}</span>
							<span v-else>{{ item[header.key] }}</span>
						</div>
					</div>
				</v-card-text>
			</v-card>
		</template>
	</v-data-table-server>
	<v-data-table-server
		v-else
		:items-length="itemsLen"
		:headers="headers"
		:items="items"
		@update:options="fetchData"
		:search="search"
		:loading="loading"
	>
		<template #item="{ item }">
			<tr>
				<td v-for="header in headers">
					<span v-if="header.formatFunc">
						{{ header.formatFunc(item[header.key]) }}
					</span>
					<v-btn
						v-else-if="header.key === 'actions'"
						icon="mdi-arrow-right"
						size="small"
						variant="outlined"
						:to="getToFunction(item)"
					></v-btn>
					<span v-else>
						{{ item[header.key] }}
					</span>
				</td>
			</tr>
		</template>
	</v-data-table-server>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import { useDisplay } from "vuetify";
const { mobile } = useDisplay();

const props = defineProps({
	headers: {
		type: Array,
		required: true,
	},
	fetch: {
		type: Function,
		required: true,
	},
	filters: {
		type: Object,
		required: true,
	},
	getToFunction: {
		type: Function,
	},
	forceMobile: {
		type: Boolean,
	},
});

const search = ref({});
const title = ref(props.headers[0]);
const data_headers = ref(props.headers.slice(1, props.headers.length - 1));

watch(props.filters, (f) => {
	search.value = structuredClone(f);
});

const loading = ref(false);
const itemsLen = ref(10);
const items = ref([]);

const fetchData = async ({ page, itemsPerPage, search }) => {
	loading.value = true;
	try {
		// Filter out falsy values
		const filterParams = Object.fromEntries(
			Object.entries(search)
				.filter(([_, value]) => (typeof value === "boolean" ? true : value))
				.map(([key, value]) => {
					// I blame python and django
					if (typeof value === "boolean") {
						if (value) {
							return [key, "True"];
						}
						return [key, "False"];
					}
					return [key, value];
				}),
		);

		// Only fetch if at least one filter is active
		if (Object.keys(filterParams).length > 0) {
			filterParams.page_size = itemsPerPage || 10;
			filterParams.page = page || 1;
			const listing = await props.fetch(filterParams);
			items.value = listing.results;
			itemsLen.value = listing.total_records;
		}
	} catch (error) {
		console.error("Error fetching items:", error);
	} finally {
		loading.value = false;
	}
};

onMounted(async () => {
	const listing = await props.fetch({ page_size: 10, page: 1 });
	items.value = listing.results;
	itemsLen.value = listing.total_records;
});
</script>
