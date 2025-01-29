<template>
    <v-card variant="flat">
        <v-card-text>
            <v-row>
                <v-col 
                    v-for="(classroom, index) in classroomsData"
                    :key="index" lg="3">
                    <SubjectsList :filter="{ classroom: classroom.id }" :title="classroom.name"/>
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { getClassrooms } from "@/apps/classrooms/api";
import SubjectsList from "@/apps/subjects/components/SubjectsList";
import { onMounted, ref, watch } from "vue";

const props = defineProps({
	filter: {
		type: Object,
		default: () => ({})
	}
});

const classroomsData = ref([]);

const fetchClassroomsData = async () => {
	const response = await getClassrooms(props.filter);
	classroomsData.value = response.results;
};

watch(() => props.filter, fetchClassroomsData, { deep: true });

onMounted(fetchClassroomsData);
</script>

