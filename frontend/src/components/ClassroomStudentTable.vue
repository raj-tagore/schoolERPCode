<template>
	<v-card>
		<v-card-title>
			Students
		</v-card-title>
		<v-card-text>
			<v-data-table :items="students" :headers="student_headers">
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
import api from '@/services/api'

export default {
	props: ['classroom'],
	data() {
		return {
			students: [],
			student_headers: [
				{ title: 'Name', value: 'user.first_name' },
				{ title: 'Actions', key: 'id', value: student => `app/students/${student.id}` },
			],
		};
	},
	methods: {
		async getStudents() {
			this.students = await Promise.all(this.classroom.students.map(async (student_id) => {
				return (await api.get(`api/accounts/students/${student_id}/`)).data;
			}));
		},
	},
	mounted() {
		this.getStudents();
	},
}
</script>
