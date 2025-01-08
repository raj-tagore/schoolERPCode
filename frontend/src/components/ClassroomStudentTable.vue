<template>
	<v-card>
		<v-card-title>
			Students
		</v-card-title>
		<v-card-text>
			<v-data-table :search="search" :items="students" :headers="student_headers">
				<template v-slot:top>
					<v-text-field
						v-model="search"
						label="Search (UPPER CASE ONLY)"
						class="mx-4"
					></v-text-field>
				</template>
				<template #[`item.id`]="{ item }">
					<v-btn :to="{ name: 'Dashboard', params: { id: item } }">
						View
					</v-btn>
				</template>
			</v-data-table>
		</v-card-text>
	</v-card>
</template>

<script>
import api from "@/services/api";

export default {
	props: ["classroom"],
	data() {
		return {
			students: [],
			search: "",
			student_headers: [
				{ title: "Name", value: "user.first_name", key: "name" },
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
		async getStudents() {
			this.students = await Promise.all(
				this.classroom.students.map(async (student_id) => {
					return (await api.get(`api/accounts/students/${student_id}/`)).data;
				}),
			);
		},
	},
	mounted() {
		this.getStudents();
	},
};
</script>
