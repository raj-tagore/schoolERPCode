
<script>
export default {
	data() {
		return {
			open: false,
		};
	},
	props: ['title'],
};
</script>

<template>
	<v-list-item @click="open = !open" class="cursor-pointer">
		<v-list-item-title>
			<div class="d-flex flex-row justify-space-between">
				<span>
					{{title}}
				</span>
				<v-icon>{{ open ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
			</div>
		</v-list-item-title>
        <v-expand-transition>
			<slot v-if="open"></slot>
        </v-expand-transition>
	</v-list-item>
</template>
