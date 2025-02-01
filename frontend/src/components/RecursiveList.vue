<template>
	<ExpandableListItem v-if="item.children && item.children.length > 0" :title="item.title">
		<v-list dense>
			<RecursiveList
				v-for="child in item.children"
				:key="child.id"
				:item="child" />
		</v-list>
	</ExpandableListItem>
	<v-list-item v-else :to="item.to">
		<v-list-item-title>{{item.title}}</v-list-item-title>
	</v-list-item>
</template>


<script setup>
import RecursiveList from "./RecursiveList.vue";
import ExpandableListItem from '@/components/c-expandable-list-item.vue'

const listProps = defineProps({
	item: Object,
});

</script>
