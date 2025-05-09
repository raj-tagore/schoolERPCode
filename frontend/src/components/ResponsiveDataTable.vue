<template>
	<v-data-table-server
		v-if="mobile || forceMobile"
		:items-length="itemsLen"
		:headers="[]"
		:items="items"
		@update:options="fetchData"
		:search="JSON.stringify(filters)"
		:loading="loading"
	>
		<template #headers={}></template>
		<template #item={item}>
			<v-card
				class="ma-2 pa-2"
				variant="outlined"
			>
				<div class="d-flex align-center justify-space-between">
					<v-card-title v-if="title.formatFunc" class="text-subtitle-1">{{ title.formatFunc(item[title.key]) }}</v-card-title>
					<v-card-title v-else class="text-subtitle-1">{{ item[title.key] }}</v-card-title>
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
		:search="JSON.stringify(filters)"
		:loading="loading"
	>
		<template #item="{ item }">
			<tr>
				<td v-for="header in headers" :class="header.key === 'actions' ? 'text-right' : null">
					<span v-if="header.formatFunc">
						{{ header.formatFunc(item[header.key]) }}
					</span>
					<v-btn
						v-else-if="header.key === 'actions'"
						icon="mdi-arrow-right"
						size="x-small"
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
import { onMounted, ref } from "vue";
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
	getToFunction: {
		type: Function,
	},
	forceMobile: {
		type: Boolean,
	},
});

const filters = defineModel();


const title = ref(props.headers[0]);
const data_headers = ref(props.headers.slice(1, props.headers.length - 1));

const loading = ref(false);
const itemsLen = ref(10);
const items = ref([]);

const convertFiltersForBackend = (filters) => {
	return Object.fromEntries(
		Object.entries(filters)
			.filter(([_, value]) => (typeof value === "boolean" ? true : value))
			.map(([key, value]) => {
				if (typeof value === "boolean") {
					return [key, value ? "True" : "False"];
				}
				return [key, value];
			}),
	);
};

const fetchData = async ({page, itemsPerPage, search}) => {
	loading.value = true;
	
	try {
		const filterParams = {
			...convertFiltersForBackend(JSON.parse(search)),
			page_size: itemsPerPage || 10,
			page: page || 1,
		};

		const { results, total_records } = await props.fetch(filterParams);
		items.value = results;
		itemsLen.value = total_records;
	} catch (error) {
		console.error("Error fetching items:", error);
		items.value = [];
		itemsLen.value = 0;
	} finally {
		loading.value = false;
	}
};

onMounted(() => fetchData({ search: filters }));
</script>
