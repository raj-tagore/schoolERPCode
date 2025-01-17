<template>
	<v-row>
		<v-col lg="6">
			<AllSubjectsCard />
		</v-col>
	</v-row>
</template>

<script>
import { defineComponent } from "vue";
import AllSubjectsCard from "@/apps/subjects/components/AllSubjectsCard.vue";

export default defineComponent({
	components: {
		AllSubjectsCard,
	},
});
</script>
