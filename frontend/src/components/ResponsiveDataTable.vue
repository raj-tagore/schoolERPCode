<template>
	<v-data-table-server
		class="d-md-none"
		:items-length="itemsLen"
		:headers="[]"
		:items="items"
		@update:options="fetchData"
		:search="search"
		:loading="loading"
	>
		<template #headers={}></template>
		<template #item={item}>
			<slot name="mobile" :item="item"></slot>
		</template>
	</v-data-table-server>
	<v-data-table-server
		class="d-none d-md-block"
		:items-length="itemsLen"
		:headers="headers"
		:items="items"
		@update:options="fetchData"
		:search="search"
		:loading="loading"
	>
		<template #item="{ item }">
			<tr>
				<td v-for="key in headers.map((h) => h.key)" :key="key">
					<slot :name="key" :item="item">
						{{ item[key] }}
					</slot>
				</td>
			</tr>
		</template>
	</v-data-table-server>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";

const props = defineProps({
	headers: {
		type: Object,
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
});

const search = ref({});

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
				.filter(([_, value]) => value)
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

		if (itemsPerPage) {
			filterParams.page_size = itemsPerPage;
		}
		if (page) {
			filterParams.page = page;
		}
		// Only fetch if at least one filter is active
		if (Object.keys(filterParams).length > 0) {
			console.log(filterParams);
			const listing = await props.fetch(filterParams);
			itemsLen.value = listing.total_records;
			items.value = listing.results;
		} else {
			items.value = []; // Clear the table when no filters
		}
	} catch (error) {
		console.error("Error fetching items:", error);
	} finally {
		loading.value = false;
	}
};

onMounted(async () => {
	items.value = [];
});
</script>
