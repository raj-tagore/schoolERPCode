<template>
	<v-card>
		<v-card-title class="pb-0">{{subject.name}}</v-card-title>
		<v-card-subtitle v-if="subject.teacher_details">{{ subject.teacher_details.user.first_name + ' ' + subject.teacher_details.user.last_name }}</v-card-subtitle>
		<v-card-text class="pb-4">
			Overview: <p class="text-grey-darken-1">{{ subject.description }}</p>
		</v-card-text>
	</v-card>
</template>


<script>
export default {
	props: ["subject"],
};
</script>
