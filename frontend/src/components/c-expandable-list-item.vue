<template>
	<div>
		<v-list-item 
			@click="toggleOpen" 
			:class="{ 'cursor-pointer': true, 'active': isOpen }"
			:ripple="true"
		>
			<template #prepend v-if="icon">
				<v-icon :icon="icon" size="small" />
			</template>

			<v-list-item-title>
				<div class="d-flex align-center justify-space-between">
					<span>{{ title }}</span>
					<v-icon 
						:icon="isOpen ? 'mdi-chevron-up' : 'mdi-chevron-down'"
						:class="{ 'rotate-icon': isOpen }"
						size="small"
					/>
				</div>
			</v-list-item-title>
		</v-list-item>

		<v-expand-transition>
			<div v-show="isOpen" class="pl-4">
				<slot></slot>
			</div>
		</v-expand-transition>
	</div>
</template>

<script setup>
import { ref } from 'vue';

// Props definition with validation
const props = defineProps({
	title: {
		type: String,
		required: true
	},
	icon: {
		type: String,
		default: null
	},
	initiallyOpen: {
		type: Boolean,
		default: false
	}
});

// State management
const isOpen = ref(props.initiallyOpen);

// Methods
const toggleOpen = () => {
	isOpen.value = !isOpen.value;
};

// Emits
defineEmits(['update:open']);
</script>
