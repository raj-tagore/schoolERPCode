<template>
  <v-card variant="flat">
    <v-card-title>
      <FilterCard 
        v-model="filters"
        :filtersInfo="filtersInfo" 
      />
    </v-card-title>
    <ResponsiveDataTable 
      :getToFunction="(item) => ({name: 'Announcement', params: {announcementId: item.id}})" 
      :headers="headers" 
      :fetch="getAnnouncements" 
      :filters="filters"
      :forceMobile="forceMobile"
    />
  </v-card>
</template>

<script setup>
import { ref, watch } from "vue";
import { getAnnouncements } from "../api";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import FilterCard from "@/components/FilterCard.vue";

const defaultFilters = {
	title: "",
	classroom: null,
	subject: null,
	signed_by: null,
	is_school_wide: null,
};

const defaultFiltersInfo = [
	{
		label: "Search by title",
		type: "string",
		key: "title",
	},
	{
		label: "Filter by classroom",
		type: "classroom",
		key: "classroom",
	},
	{
		label: "Filter by subject",
		type: "subject",
		key: "subject",
	},
	{
		label: "Filter by signer",
		type: "teacher",
		key: "signed_by",
	},
	{
		label: "Is School Wide",
		type: "n_nary",
		key: "is_school_wide",
		fetchOptions: () => [
			{ title: "All Announcements", value: null },
			{ title: "School Wide Only", value: "True" },
			{ title: "Non-School Wide Only", value: "False" },
		],
	},
];

const props = defineProps({
	forceMobile: {
		type: Boolean,
		default: false,
	},
	initialFilters: {
		type: Object,
		default: () => ({}),
	},
	initialFiltersInfo: {
		type: Array,
		default: () => ([]),
	},
});

const filters = ref({ ...defaultFilters, ...props.initialFilters });

const filtersInfo = ref(defaultFiltersInfo.map(defaultFilter => {
  const override = props.initialFiltersInfo.find(f => f.key === defaultFilter.key);
  return override ? { ...defaultFilter, ...override } : defaultFilter;
}));

const formatDate = (dateString) =>
	Intl.DateTimeFormat("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
	}).format(Date.parse(dateString));

const headers = [
	{ title: "Title", key: "title" },
	{ title: "Release Date", key: "release_at", formatFunc: formatDate },
	{ title: "Expiry Date", key: "expiry_at", formatFunc: formatDate },
	{
		title: "Signed By",
		key: "signed_by_details",
		formatFunc: (signedBy) => signedBy.user_details.full_name,
	},
	{ title: "Actions", key: "actions", sortable: false },
];
</script>
