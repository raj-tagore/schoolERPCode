<template>
	<v-card>
		<v-card-title>
			{{subject.name}}
		</v-card-title>
		<v-card-subtitle class="pb-4">
			<b>Description: </b>{{ subject.description }}
		</v-card-subtitle>
	</v-card>
</template>


<script>
export default {
	props: ["subject"],
};
</script>
