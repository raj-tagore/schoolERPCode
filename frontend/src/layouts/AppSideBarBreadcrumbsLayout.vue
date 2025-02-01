<template>
	<AppSideBarLayout>
		<BreadcrumbsLayout>
			<router-view></router-view>
		</BreadcrumbsLayout>
	</AppSideBarLayout>
</template>

<script setup>
import BreadcrumbsLayout from "@/layouts/BreadcrumbsLayout.vue";
import AppSideBarLayout from "@/layouts/AppSideBarLayout.vue";
</script>
