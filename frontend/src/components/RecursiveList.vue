<template>
	<ExpandableListItem v-if="item.children" :title="item.title">
		<v-list dense>
			<v-list-item :to="{name: item.to}">
				<v-list-item-title>{{item.title}}</v-list-item-title>
			</v-list-item>
			<RecursiveList
				v-for="child in item.children"
				:key="child.id"
				:item="child" />
		</v-list>
	</ExpandableListItem>
	<v-list-item v-else :to="{name: item.to}">
		<v-list-item-title>{{item.title}}</v-list-item-title>
	</v-list-item>
</template>


<script setup>
import RecursiveList from "./RecursiveList.vue";

const listProps = defineProps({
	item: Object,
});

</script>
