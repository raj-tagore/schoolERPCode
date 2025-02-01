<template>
	<v-container>
		<v-row>
			<v-col>
				<v-row>
					<v-col cols="12" md="4">
						<StatsCard title="Teachers" :fetchStats="getTeacherStats" />
					</v-col>
					<v-col cols="12" md="8">
						<TeachersLookup />
					</v-col>
				</v-row>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import TeachersLookup from "@/apps/teachers/components/TeachersLookup.vue";
import StatsCard from "@/components/StatsCard.vue";
import { getTeacherStats } from "@/apps/teachers/api";
</script>
