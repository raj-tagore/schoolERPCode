<template>
	<v-container>
		<v-card>
			<v-card-title>Subject Search</v-card-title>
			<v-card-text>
				<v-row>
					<v-col>
					<v-text-field
						v-model="search"
						label="Search for your classroom"
						density="comfortable"
					/>
					</v-col>
				</v-row>
				<v-row>
					<v-col 
						v-for="(classroom, index) in classroomsData.slice(0,4)" 
						cols="12" lg="6"
						:key="index">
						<SubjectsList :filter="{ classroom: classroom.id }" :title="classroom.name"/>
					</v-col>
				</v-row>
			</v-card-text>
		</v-card>
	</v-container>
</template>

<script setup>
import { getClassrooms } from "@/apps/classrooms/api";
import SubjectsList from "@/apps/subjects/components/SubjectsList";
import { onMounted, ref, computed } from "vue";

const classroomsDataRaw = ref([]);
const search = ref("");

const classroomsData = computed({
	get: () => {
		console.log(search.value.length);
		if (search.value.length === 0) {
			return classroomsDataRaw.value;
		}
		return classroomsDataRaw.value.filter((v) =>
			`${v.name}${v.standard}`.includes(search.value),
		);
	},
});

const fetchClassroomsData = async () => {
	classroomsDataRaw.value = await getClassrooms();
	console.log(classroomsDataRaw);
};
onMounted(fetchClassroomsData);
</script>

