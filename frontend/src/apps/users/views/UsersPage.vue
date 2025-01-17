<template>
	<v-container>
		<v-row>
			<v-col cols="12" lg="6">
				<TeachersTable />
			</v-col>
			<v-col cols="12" lg="6">
				<StudentsTable />
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import StudentsTable from "@/apps/users/components/StudentsTable.vue";
import TeachersTable from "@/apps/users/components/TeachersTable.vue";

</script>
