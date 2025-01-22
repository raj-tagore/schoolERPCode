<template>
	<v-row>
		<v-col>
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
