<template>
    <v-card>
        <v-card-title>{{ title }}</v-card-title>
        <v-card-text>
            <v-list density="compact">
                <v-list-item 
                    v-for="(subject, index) in subjects" 
                    :key="index"
                    class="ma-1 pa-2 border"
                >
					<v-list-item-title>{{ subject.name }}</v-list-item-title>
					<v-list-item-subtitle>
						{{ subject.teacher_details?.user_details?.full_name }}
					</v-list-item-subtitle>
                    <template v-slot:append>
                        <v-btn 
                        :to="{ name: 'Subject', params: { subjectId: subject.id } }"
                        icon="mdi-arrow-right"
                        size="small"
                        variant="text"
                        class="ma-1 pa-2 border"
                        ></v-btn>
                    </template>
                </v-list-item>
            </v-list>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getSubjects } from "../api";

// Props
const props = defineProps({
	filter: Object,
	title: {
		type: String,
		default: "Subjects",
	},
});

const subjects = ref([]);
const fetchSubjects = async () => {
	subjects.value = (await getSubjects(props.filter)).results;
};
onMounted(fetchSubjects);
</script>
