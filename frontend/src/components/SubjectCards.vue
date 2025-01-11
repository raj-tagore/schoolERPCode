<template>
    <v-card>
        <v-card-title >Subjects</v-card-title>
        <v-card-text>
            <v-row>
            <v-col 
            v-for="(subject, index) in subjectsData" 
            :key="index" 
            cols="6" >
                <v-card>
                <v-card-title class="text-body-1 pb-0">{{ subject.name }}</v-card-title>
                <v-card-subtitle>{{ subject.teacher_details?.user?.full_name }}</v-card-subtitle>
                <v-card-actions class="d-flex justify-center">
                    <v-btn :to="{ name: 'Subject', params: { subjectId: subject.id }}">Enter</v-btn>
                </v-card-actions>
                </v-card>
            </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<script>
import { ref, onMounted } from "vue";
import api from "@/services/api";

export default {
	name: "SubjectCards",
	props: ["url"],
	setup(props) {

		const subjectsData = ref([]);

		const getSubjectsData = async () => {
			try {
				const response = await api.get(props.url);
				subjectsData.value = response.data;
				console.log("Subjects data:", subjectsData.value);
			} catch (error) {
				console.error("Error fetching subjects data:", error);
			}
		};

		onMounted(() => {
			getSubjectsData();
		});

		return {
			subjectsData,
		};
	},
};
</script>
      
