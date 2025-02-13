<template>
	<v-card>
		<v-card-title class="pb-0">{{subject.name}} ({{subject.classroom_details?.name}})</v-card-title>
		<v-card-subtitle class="pt-2">
			<v-chip 
				v-if="subject.teacher_details"
				link
				:to="{ 
					name: 'Teacher', 
					params: { 
						teacherId: subject.teacher_details?.id 
					}
				}"
			>
				Teacher: {{ subject.teacher_details?.user_details?.full_name }}
			</v-chip>
		</v-card-subtitle>
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
