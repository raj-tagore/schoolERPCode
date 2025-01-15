<template>
	<v-container>
		<v-card>
			<v-card-title>
				Teachers
			</v-card-title>
			<v-card-text>
				<v-data-table density="comfortable" :search="search" :items="teachers" :headers="teacher_headers">
					<template v-slot:top>
						<v-container>
							<v-text-field
								v-model="search"
								label="Search"
								density="comfortable"
							></v-text-field>
							<v-btn
								v-bind="activatorProps"
								@click="$emit('addTeacher')"
							>
								<v-icon>mdi-plus</v-icon>
								Add Teacher
							</v-btn>
						</v-container>
					</template>
					<template #[`item.id`]="{ item }">
						<v-btn class="mx-2" size="x-small" icon="mdi-eye" :to="{ name: 'Dashboard', params: { id: item} }"></v-btn>
						<v-btn v-if='showRemoveTeacher' class="mx-2" size="x-small" icon="mdi-delete" color="red" @click="$emit('removeTeacher', item.id)"></v-btn>
					</template>
				</v-data-table>
			</v-card-text>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref, watch } from "vue";

import { getTeachers, getClassroomTeachers } from "@/apps/users/api";

const props = defineProps({
	showAddTeacher: Boolean,
	showRemoveTeacher: Boolean,
	classroom: Object,
	filter: Object,
});

let teachers = ref([]);
const search = ref("");
const teacher_headers = ref([
	{ title: "Name", value: "user.full_name", key: "name" },
	{
		title: "",
		key: "id",
		align: "end",
		sortable: false,
		value: (teacher) => `app/teachers/${teacher.id}`,
	},
]);

if (props) {
	if (props.classroom) {
		teachers = await getClassroomTeachers(props.classroom);
	} else {
		teachers = await getTeachers(props.filter);
	}
}
</script>
