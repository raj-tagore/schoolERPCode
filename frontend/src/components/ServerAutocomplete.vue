<template>
	<v-autocomplete
		:value="selectedItem"
		:items="results"
		:loading="loading"
		:search-input.sync="query"
		:label="label"
		:item-props="getInfo"
		@input="selectedItem = $event.target.value"
		<!--- update:modelValue is a special event that is emitted when you want to indicate to vue that model's value has been changed --->
		@update:modelValue="emit('update:modelValue', $event)"
		@update:search="debouncedFetchResults"

	>
		<template v-slot:append-item>
			<div v-if="hasMore" v-intersect="debouncedFetchResults" class="pa-4 teal--text">
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

// Text used to search for items
const query = ref("");

// Filters passed to the fetch function
const filters = ref({ page_size: 10, page: 1 });

const results = ref([]);

const selectedItem = ref(null);

// To shut up the linter
_ = selectedItem;

const loading = ref(false);

// Flag to indicate if there are more items to fetch
const hasMore = ref(true);

// For debouncing
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

// Allow for fetch every 300ms
// Allow for re-triggering fetch if the user scrolls to the bottom of the list
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

onMounted(fetchResults);
</script>
