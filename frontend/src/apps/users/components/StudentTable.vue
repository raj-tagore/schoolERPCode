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

<script>

import { watch } from "vue";
import { getStudents, getClassroomStudents } from "@/apps/users/api";

export default {
	props: ["showAddStudent", "showRemoveStudent", "classroom", "filter"],
	data() {
		return {
			students: [],
			search: "",
			student_headers: [
				{ title: "Name", value: "user.full_name", key: "name" },
				{
					title: "",
					key: "id",
					align: "end",
					sortable: false,
					value: (student) => `app/students/${student.id}`,
				},
			],
		};
	},
	methods: {
		studentInfoFromObj(item) {
			console.log(item);
			const result = {
				title: item.user.full_name,
				subtitle: item.identifier,
				value: item.id,
			};
			return result;
		},
	},
	mounted() {
		if (this.classroom) {
			this.students = getClassroomStudents(classroom);
		} else {
			this.students = getStudents(filter);
		}

		watch(this.classroom, () => {
			this.getStudents();
		});
		watch(this.filter, () => {
			this.students = getStudents(filter);
		});
	},
};
</script>
