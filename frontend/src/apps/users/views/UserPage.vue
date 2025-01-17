<template>
	<v-container>
		<v-row align="center" justify="center">
			<v-col>
				<v-card>
					<v-tabs
						background-color="deep-purple accent-4"
						center-active
						dark
						density="comfortable"
						align-tabs="center"
						v-model="tabs"
					>
						<v-tab>Profile</v-tab>
						<v-tab>Settings</v-tab>
					</v-tabs>
				</v-card>
				<v-tabs-window v-model="tabs">
					<v-tabs-window-item>
						<UserCard :userId="props.userId" />
					</v-tabs-window-item>
					<v-tabs-window-item>
					</v-tabs-window-item>
				</v-tabs-window>
			</v-col>
		</v-row>

	</v-container>
</template>

<script setup>
import { ref } from "vue";
console.log("UserPage")

import UserCard from "@/apps/users/components/UserCard.vue";

const props = defineProps({
	userId: Number,
});

console.log("UserPage", props)

const tabs = ref(null);

</script>
