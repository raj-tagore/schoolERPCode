<template>
	<v-card>
		<v-card-title>
			{{subject.name}}
			<p class="text-body-2 pb-4">
				<b>Name: </b>{{subject.name}} <br>
				<b>Description: </b>{{ subject.description }}
			</p>
		</v-card-title>
	</v-card>
</template>


<script>
export default {
	props: ["subject"],
};
</script>
