<template>
	<v-card variant="flat">
		<v-card-title>
			<FilterCard 
				v-model="filters"
				:filtersInfo="filtersInfo" 
			/>
		</v-card-title>
		<ResponsiveDataTable 
			:getToFunction="(item) => ({name: 'Record', params: {recordId: item.id}})" 
			:headers="headers" 
			:fetch="getRecords" 
			v-model="filters"
      		:forceMobile="forceMobile"
    	/>
	</v-card>
</template>

<script setup>
import { ref } from "vue";
import { getRecords } from "@/apps/finances/api.js";
import ResponsiveDataTable from "@/components/ResponsiveDataTable.vue";
import FilterCard from "@/components/FilterCard.vue";

const filters = ref({
	student: null,
	amount_start: null,
	amount_end: null,
	datetime_start: null,
	datetime_end: null,
	payment_type: null,
	order_id: null,
	payment_status: null,
	purpose: null,
	payee: null,
});

const filtersInfo = ref([
	{
		label: "Filter by student",
		type: "student",
		key: "student",
	},
	{
		label: "Filter by minimum amount",
		type: "integer",
		key: "amount_start",
	},
	{
		label: "Filter by maximum amount",
		type: "integer",
		key: "amount_end",
	},
	{
		label: "Filter by Date",
		type: "dates",
		key: ["datetime_start", "datetime_end"],
	},
	{
		label: "Filter by payment type",
		type: "n_nary",
		key: "payment_type",
		fetchOptions: () => [
			{ title: "Select", value: null },
			{ title: "UPI", value: "upi" },
			{ title: "Netbanking", value: "netbanking" },
			{ title: "Credit/Debit Card", value: "card" },
			{ title: "Digital Wallet", value: "wallet" },
		],
	},
	{
		label: "Filter by order ID",
		type: "string",
		key: "order_id",
	},
	{
		label: "Filter by payment status",
		type: "n_nary",
		key: "payment_status",
		fetchOptions: () => [
			{ title: "Select", value: null },
			{ title: "Success", value: "S" },
			{ title: "Pending", value: "P" },
			{ title: "Failed", value: "F" },
		],
	},
	{
		label: "Filter by purpose",
		type: "payment_purpose",
		key: "purpose",
	},
	{
		label: "Filter by payee",
		type: "payee",
		key: "payee",
	},
]);

const props = defineProps({
	forceMobile: {
		type: Boolean,
		default: false,
	},
});

// Properly parses the date string, Date() constructor doesn't work well with ISO strings
const formatDate = (dateString) =>
	Intl.DateTimeFormat("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
	}).format(Date.parse(dateString));

const headers = [
	{
		title: "Student",
		key: "student_details",
		formatFunc: (student) => student.user_details.full_name,
	},
	{ title: "Amount", key: "amount", formatFunc: (a) => a / 100 },
	{ title: "Date", key: "datetime", formatFunc: formatDate },
	{ title: "Payment Type", key: "payment_type" },
	{ title: "Payment Status", key: "payment_status" },
	{ title: "Payee", key: "payee_details", formatFunc: (payee) => payee.email },
	{ title: "Actions", key: "actions", sortable: false },
];
</script>
