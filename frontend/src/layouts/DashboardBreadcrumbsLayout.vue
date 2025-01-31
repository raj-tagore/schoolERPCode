<template>
	<DashboardLayout>
		<BreadcrumbsLayout>
			<router-view></router-view>
		</BreadcrumbsLayout>
	</DashboardLayout>
</template>

<script setup>
import BreadcrumbsLayout from "@/layouts/BreadcrumbsLayout.vue";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
</script>
