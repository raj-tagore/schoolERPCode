<template>
	<v-app>
		<v-app-bar app color="grey" density="compact">
			<v-toolbar-title class="flex text-center">
				<h4>Classroom</h4>
			</v-toolbar-title>
		</v-app-bar>

		<v-main>
			<router-view></router-view>
		</v-main>
	</v-app>
</template>


<script>
// For Options API style components, remove this block entirely since we are using the <script setup> syntax above.
// This block is intentionally left empty as all logic is now in <script setup>.
</script>

<style>
/* Add any custom styles if necessary */
</style>
