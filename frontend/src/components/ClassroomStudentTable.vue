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
						<v-dialog>
							<template v-slot:activator="{ props: activatorProps }">
								<v-btn
									v-bind="activatorProps"
								>
									<v-icon>mdi-plus</v-icon>
									Add Student
								</v-btn>
							</template>
							<template v-slot:default="{ isActive }">
								<v-sheet class="mx-auto">
									<v-container>
										<v-row>
											<v-col>
												<v-autocomplete label="New Student" :item-props="studentInfoFromObj" :items="allStudents" v-model="newStudent"></v-autocomplete>
											</v-col>
										</v-row>

										<v-row>
											<v-col>
												<v-btn @click="$emit('addStudent', this.newStudent)">Submit</v-btn>
											</v-col>
											<v-col>
												<v-btn
													@click="isActive.value = false">
													Cancel
												</v-btn>
											</v-col>
										</v-row>
									</v-container>
								</v-sheet>
							</template>

						</v-dialog>
					</v-container>
				</template>
				<template #[`item.id`]="{ item }">
						<v-btn class="mx-2" size="x-small" icon="mdi-eye" :to="{ name: 'Dashboard', params: { id: item} }"></v-btn>
						<v-btn class="mx-2" size="x-small" icon="mdi-delete" color="red" @click="$emit('removeStudent', item.id)"></v-btn>
				</template>
			</v-data-table>
		</v-card-text>
	</v-card>
</v-container>
</template>

<script>
import api from "@/services/api";
import { watch } from "vue";

export default {
	props: ["classroom"],
	data() {
		return {
			students: [],
			allStudents: [],
			search: "",
			newStudent: null,
			student_headers: [
				{
					title: "Name",
					value: (teacher) =>
						`${teacher.user.first_name} ${teacher.user.last_name}`,
					key: "name",
				},
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
				title: `${item.user.first_name} ${item.user.last_name}`,
				subtitle: item.identifier,
				value: item.id,
			};
			return result;
		},
		async getAllStudents() {
			this.allStudents = (await api.get("api/accounts/students/all")).data;
		},
		async submit(event) {
			this.loading = true;

			const results = await event;

			this.loading = false;

			alert(JSON.stringify(results, null, 2));
		},
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
		this.getAllStudents();

		watch(this.classroom, () => {
			this.getStudents();
		});
	},
};
</script>
