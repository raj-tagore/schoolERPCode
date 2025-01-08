<template>
	<v-card>
		<v-card-title>
			Teachers
		</v-card-title>
		<v-card-text>
			<v-data-table :items="teachers" :headers="teacher_headers">
				<template #[`item.id`]="{ item }">
					<v-btn :to="{ name: 'Dashboard', params: { id: item} }">
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
			teachers: [],
			teacher_headers: [
				{ title: 'Name', value: 'user.first_name' },
				{ title: 'Actions', key: 'id', value: teacher => `app/teachers/${teacher.id}` },
			],
		};
	},
	methods: {
		async getTeachers() {
			this.teachers = await Promise.all(this.classroom.other_teachers.map(async (teacher_id) => {
				return (await api.get(`api/accounts/teachers/${teacher_id}/`)).data;
			}));
		},
	},
	mounted() {
		this.getTeachers();
	},
}
</script>
