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
						</v-container>
					</template>
					<template #[`item.id`]="{ item }">
						<v-btn class="mx-2" size="x-small" icon="mdi-eye" :to="{ name: 'Dashboard', params: { id: item} }"></v-btn>
					</template>
				</v-data-table>
			</v-card-text>
		</v-card>
	</v-container>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { getTeachers } from "@/apps/users/api";

const props = defineProps({
    filter: Object
});

const teachers = ref([]);
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

const fetchTeachers = async () => {
    teachers.value = await getTeachers(props.filter || {});
};

onMounted(fetchTeachers);

</script>