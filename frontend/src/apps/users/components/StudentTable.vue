<template>
	<v-container>
	<v-card>
		<v-card-title>
			Students
		</v-card-title>
		<v-card-text>
			<v-data-table density="comfortable" :search="search" :items="students" :headers="student_headers">
				<template v-slot:top>
					<v-container>
						<v-text-field
							v-model="search"
							label="Search"
							density="comfortable"
						></v-text-field>
							<v-btn
								v-bind="activatorProps"
								@click="$emit('addStudent')"
							>
								<v-icon>mdi-plus</v-icon>
								Add Student
							</v-btn>
					</v-container>
				</template>
				<template #[`item.id`]="{ item }">
						<v-btn class="mx-2" size="x-small" icon="mdi-eye" :to="{ name: 'Dashboard', params: { id: item} }"></v-btn>
						<v-btn v-if="showRemoveStudent" class="mx-2" size="x-small" icon="mdi-delete" color="red" @click="$emit('removeStudent', item.id)"></v-btn>
				</template>
			</v-data-table>
		</v-card-text>
	</v-card>
</v-container>
</template>

<script setup>
import { ref, watch } from "vue";
import { getStudents, getClassroomStudents } from "@/apps/users/api";

const { props } = defineProps({
	showAddStudent: Boolean,
	showRemoveStudent: Boolean,
	classroom: Object,
	filter: Object,
});

let students = ref([]);
const search = ref("");
const student_headers = ref([
	{ title: "Name", value: "user.full_name", key: "name" },
	{
		title: "",
		key: "id",
		align: "end",
		sortable: false,
		value: (student) => `app/students/${student.id}`,
	},
]);

if (props) {
	if (props.classroom) {
		students = await getClassroomStudents(props.classroom);
		watch(props.classroom, async () => {
			students = await getStudents();
		});
	} else {
		students = await getStudents(props.filter);
		watch(props.filter, async () => {
			students = await getStudents(props.filter);
		});
	}
}
</script>
