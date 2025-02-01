<template>
	<v-container>
		<v-row>
			<v-col>
				<v-row class="ma-2 flex justify-center">
					<v-col lg="6">
						<v-card variant="flat">
							<v-card-title>{{ assignment?.title }}</v-card-title>
							<v-card-text>{{ assignment?.description }}</v-card-text>
						</v-card>
					</v-col>
					<v-col lg="3" v-if="assignment">
						<v-card variant="flat">
							<h4 class="text-subtitle-1 mt-4">Dates:</h4>
							<v-chip color="primary">Release: {{ formatDate(assignment.release_at) }}</v-chip>
							<v-chip color="red">Due: {{ formatDate(assignment.due_at) }}</v-chip>

							<v-spacer class="pt-5"></v-spacer>
							<v-divider :thickness="5"></v-divider>
							<div v-if="assignment.subject_details">
								<SubjectsList title="Subject" :filter="{id: assignment.subject}"></SubjectsList>
							</div>
						</v-card>
					</v-col>
				</v-row>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import SubjectsList from "@/apps/subjects/components/SubjectsList.vue";
import { getAssignment } from "@/apps/assignments/api";

const assignment = ref(null);

const props = defineProps({
	assignmentId: Number,
});

// Properly parses the date string, Date() constructor doesn't work well with ISO strings
const formatDate = (dateString) =>
	Intl.DateTimeFormat("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
		hour: "2-digit",
		minute: "2-digit",
		second: "2-digit",
	}).format(Date.parse(dateString));

const fetchDetails = async () => {
	assignment.value = await getAssignment(props.assignmentId);
};

onMounted(fetchDetails);
</script>
