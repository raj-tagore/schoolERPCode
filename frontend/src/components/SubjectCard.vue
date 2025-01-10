<template>
	<v-card>
		<v-card-title>
			{{subject.name}}
		</v-card-title>
		<v-card-subtitle v-if="subject.teacher_details">{{ subject.teacher_details.user.first_name + ' ' + subject.teacher_details.user.last_name }}</v-card-subtitle>
		<v-card-actions class="justify-center">
			<v-btn :to="{name: 'Subject', params: {subjectId: subject.id}}">Enter</v-btn>
		</v-card-actions>
		<v-card-text class="pb-4">
			<b>Description: </b>{{ subject.description }}
		</v-card-text>
	</v-card>
</template>


<script>
export default {
	props: ["subject"],
};
</script>
