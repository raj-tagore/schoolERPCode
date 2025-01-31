<template>
	<v-container>
		<v-row>
			<v-col>
				<v-row>
					<v-col cols="12" md="4">
						<StatsCard title="Parents" :fetchStats="getParentStats" />
					</v-col>
					<v-col cols="12" md="8">
						<ParentsLookup />
					</v-col>
				</v-row>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import ParentsLookup from "@/apps/parents/components/ParentsLookup.vue";
import StatsCard from "@/components/StatsCard.vue";
import { getParentStats } from "@/apps/parents/api";
</script>
