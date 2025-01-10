<template>
	<v-card>
		<v-card-title>
			Teachers
		</v-card-title>
		<v-card-text>
			<v-data-table :search="search" :items="teachers" :headers="teacher_headers">
				<template v-slot:top>
					<v-text-field
						v-model="search"
						label="Search"
						class="mx-4"
					></v-text-field>
				</template>
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
import api from "@/services/api";

export default {
	props: ["classroom"],
	data() {
		return {
			teachers: [],
			search: "",
			teacher_headers: [
				{ title: "Name", value: "user.first_name", key: "name" },
				{
					title: "",
					key: "id",
					align: "end",
					sortable: false,
					value: (teacher) => `app/teachers/${teacher.id}`,
				},
			],
		};
	},
	methods: {
		async getTeachers() {
			this.teachers = await Promise.all(
				this.classroom.other_teachers.map(async (teacher_id) => {
					return (await api.get(`api/accounts/teachers/${teacher_id}/`)).data;
				}),
			);
		},
	},
	mounted() {
		this.getTeachers();
	},
};
</script>
