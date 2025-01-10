<template>
	<v-container>
	<v-card>
		<v-card-title>
			Teachers
		</v-card-title>
		<v-card-text>
			<v-data-table :search="search" :items="teachers" :headers="teacher_headers">
				<template v-slot:top>
					<v-container class="d-flex">
						<v-text-field
							v-model="search"
							label="Search"
							class="mx-4"
						></v-text-field>
						<v-dialog>
							<template v-slot:activator="{ props: activatorProps }">
								<v-btn
									v-bind="activatorProps"
								>
									<v-icon>mdi-plus</v-icon>
									Add Teacher
								</v-btn>
							</template>
							<template v-slot:default="{ isActive }">
								<v-sheet class="mx-auto">
									<v-container>
										<v-row>
											<v-col>
												<v-autocomplete label="New Teacher" :item-props="teacherInfoFromObj" :items="allTeachers" v-model="newTeacher"></v-autocomplete>
											</v-col>
										</v-row>

										<v-row>
											<v-col>
												<v-btn @click="$emit('addTeacher', this.newTeacher)">Submit</v-btn>
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
						<v-btn class="mx-2" size="x-small" icon="mdi-delete" color="red" @click="$emit('removeTeacher', item.id)"></v-btn>
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
			teachers: [],
			allTeachers: [],
			search: "",
			newTeacher: null,
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
		teacherInfoFromObj(item) {
			console.log(item);
			const result = {
				title: `${item.user.first_name} ${item.user.last_name}`,
				subtitle: item.identifier,
				value: item.id,
			};
			return result
		},
		async getAllTeachers() {
			this.allTeachers = (await api.get("api/accounts/teachers/all")).data;
		},
		async submit(event) {
			this.loading = true;

			const results = await event;

			this.loading = false;

			alert(JSON.stringify(results, null, 2));
		},
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
		this.getAllTeachers();

		watch(this.classroom, () => {
			this.getTeachers();
		});
	},
};
</script>
