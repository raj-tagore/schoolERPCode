<template>
  <v-card variant="flat">
    <v-card-title>
      <FilterCard 
        v-model="filters"
        :filtersInfo="filtersInfo" 
      /> 
    </v-card-title>
    <ResponsiveDataTable 
      :getToFunction="(item) => ({name: 'Calendar', params: {calendarId: item.id}})" 
      :headers="headers" 
      :fetch="getCalendars" 
      v-model="filters"
      :forceMobile="forceMobile"
    />
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import { getCalendars } from "../api";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import FilterCard from "@/components/FilterCard.vue";

const defaultFilters = {
  name: "",
  classroom: null,
  subject: null,
  created_by: null,
  is_school_wide: null,
};

const defaultFiltersInfo = [
  {
    label: "Search by name",
    type: "string",
    key: "name",
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
      { title: "All Calendars", value: null },
      { title: "School Wide Only", value: "True" },
      { title: "Class Specific Only", value: "False" },
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

const headers = [
  { title: "Name", key: "name" },
  { title: "Description", key: "description" },
  { 
    title: "Created By", 
    key: "created_by_details",
    formatFunc: (createdBy) => createdBy?.user_details?.full_name,
  },
  { 
    title: "Type", 
    key: "is_school_wide",
    formatFunc: (isSchoolWide) => isSchoolWide ? "School Wide" : "Class Specific",
  },
  { title: "Actions", key: "actions", sortable: false },
];
</script>
