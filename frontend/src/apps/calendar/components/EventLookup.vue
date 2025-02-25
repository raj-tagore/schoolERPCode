<template>
  <v-card variant="flat">
    <v-card-title>
      <FilterCard 
        v-model="filters"
        :filtersInfo="filtersInfo" 
      /> 
    </v-card-title>
    <ResponsiveDataTable 
      :getToFunction="(item) => ({name: 'Event', params: {eventId: item.id}})" 
      :headers="headers" 
      :fetch="getEvents" 
      v-model="filters"
      :forceMobile="forceMobile"
    />
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import { getEvents } from "../api";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import FilterCard from "@/components/FilterCard.vue";

const defaultFilters = {
  title: "",
  classroom: null,
  subject: null,
  created_by: null,
  is_school_wide: null,
  start: null,
  end: null,
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
    label: "Filter by creator",
    type: "teacher",
    key: "created_by",
  },
  {
    label: "Is School Wide",
    type: "n_nary",
    key: "is_school_wide",
    fetchOptions: () => [
      { title: "All Events", value: null },
      { title: "School Wide Only", value: "True" },
      { title: "Non-School Wide Only", value: "False" },
    ],
  },
  {
    label: "Date Range",
    type: "dates",
    key: ["start", "end"],
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
    hour: "numeric",
    minute: "numeric",
  }).format(new Date(dateString));

const headers = [
  { title: "Title", key: "title" },
  { title: "Start Time", key: "start", formatFunc: formatDate },
  { title: "End Time", key: "end", formatFunc: formatDate },
  { title: "Actions", key: "actions", sortable: false },
];
</script>
