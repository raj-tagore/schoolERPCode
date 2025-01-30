<template>
	<v-autocomplete
		v-model="selectedItem"
		:items="results"
		:loading="loading"
		:search-input.sync="query"
		:label="label"
		:item-props="getInfo"
		@update:search="debouncedFetchResults"
		@click:clear="searchChanged"
	>
		<template v-slot:append-item>
			<div v-if="hasMore" v-intersect="onIntersect" class="pa-4 teal--text">
				Loading more items ...
			</div>
		</template>
	</v-autocomplete>
</template>
<script setup>
import { ref, onMounted } from "vue";

const emit = defineEmits(["update:modelValue"]);

const props = defineProps({
	getInfo: {
		type: Function,
		required: true,
	},
	modelValue: {
		type: Number,
		required: true,
	},
	fetch: {
		type: Function,
		required: true,
	},
	searchField: {
		type: String,
		required: true,
	},
	label: {
		type: String,
		required: true,
	},
});

const query = ref("");
const filters = ref({ page_size: 10, page: 1 });
const results = ref([]);
const selectedItem = ref(null);
const loading = ref(false);
const hasMore = ref(true);

const triggered = ref(false);
const reTriggered = ref(false);

const fetchResults = async () => {
	if (loading.value || !hasMore.value) return;
	filters.value[props.searchField] = query.value;
	loading.value = true;
	try {
		const listing = await props.fetch(filters.value);
		if (listing.results.length > 0) {
			results.value = [...results.value, ...listing.results];
			filters.value.page++;
		} else {
			hasMore.value = false;
		}
	} catch (error) {
		console.error("API Error:", error);
	} finally {
		loading.value = false;
	}
};

const debouncedFetchResults = () => {
	if (triggered.value) {
		reTriggered.value = true;
		return;
	}
	triggered.value = true;
	fetchResults();
	setTimeout(() => {
		triggered.value = false;
		if (reTriggered.value) {
			reTriggered.value = false;
			debouncedFetchResults();
		}
	}, 300);
};

const searchChanged = () => {
	hasMore.value = true;
	debouncedFetchResults();
};

const onIntersect = () => {
	debouncedFetchResults();
};

onMounted(fetchResults);
</script>
