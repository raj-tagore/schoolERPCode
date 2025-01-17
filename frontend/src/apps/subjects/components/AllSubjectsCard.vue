<template>
	<v-container>
		<v-card>
			<v-card-text>
				<v-container>
					<v-row>
						<v-col>
						<v-text-field
							v-model="search"
							label="Search"
						/>

						</v-col>
					</v-row>
					<v-row class="ma-2">
						<v-col 
							v-for="(classroom, index) in classroomsData" 
							cols="12" lg="3" md="6"
							:key="index">
							<SubjectsList :filter="{ classroom: classroom.id }" :title="classroom.name"/>
						</v-col>
					</v-row>

				</v-container>
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

