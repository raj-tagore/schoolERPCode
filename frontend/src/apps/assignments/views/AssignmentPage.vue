<template>
	<v-container>
		<v-row>
			<v-col>
				<v-row class="ma-2 flex justify-center">
					<v-col lg="8">
						<v-card variant="flat">
							<v-card-title>{{ assignment?.title }}</v-card-title>
							<v-card-text>
								{{ assignment?.description }}
								
								<h4 class="text-subtitle-1 mt-4">Attachments:</h4>
								<div v-if="assignment?.attachments?.length > 0">
									<v-list>
										<v-list-item
											v-for="attachment in assignment.attachments"
											:key="attachment.id"
											:title="attachment.name"
											:subtitle="attachment.file_type"
											prepend-icon="mdi-file-document-outline"
											:href="attachment.file"
											target="_blank"
											link
										/>
									</v-list>
								</div>
								<div v-else>
									<v-chip color="info">No attachments</v-chip>
								</div>
							</v-card-text>
							<v-card-actions>
								<v-btn 
									:to="{ name: 'EditAssignment', params: { assignmentId: assignment.id } }"
									variant="outlined"
									prepend-icon="mdi-pencil"
									v-if="authStore.hasPermission('change_assignment')"
								>
									Edit
								</v-btn>
								<v-btn 
									variant="outlined" 
									prepend-icon="mdi-delete" 
									color="error"
									v-if="authStore.hasPermission('delete_assignment')"
								>
									Delete
								</v-btn>
							</v-card-actions>
						</v-card>
					</v-col>
					<v-col lg="4">
						<v-card variant="flat">
							<v-card-text>
								<h4 class="text-subtitle-1">Subject Teacher:</h4>
								<v-list lines="2">
									<v-list-item 
										link
										v-if="assignment?.subject_details?.classroom_details?.class_teacher_details"
										:title="assignment?.subject_details?.classroom_details?.class_teacher_details?.user_details?.full_name"
										:subtitle="assignment?.subject_details?.classroom_details?.class_teacher_details?.user_details?.email"
										variant="flat"
										rounded="lg"
										:to="{ 
											name: 'Teacher', 
											params: { 
												teacherId: assignment?.subject_details?.classroom_details?.class_teacher_details?.id 
											}
										}"
									/>
								</v-list>

								<h4 class="text-subtitle-1 mt-4">Dates:</h4>
								<v-chip color="primary">Release: {{ formatDate(assignment?.release_at) }}</v-chip>
								<v-chip color="red">Due: {{ formatDate(assignment?.due_at) }}</v-chip>

								<h4 class="text-subtitle-1 mt-4">Subject:</h4>
								<div v-if="assignment?.subject_details">
									<v-chip
										color="secondary"
										variant="outlined"
										:to="{ name: 'Subject', params: { subjectId: assignment.subject }}"
										link
									>
										{{ assignment.subject_details?.name }} 
										({{ assignment.subject_details?.classroom_details?.name }})
									</v-chip>
								</div>

								<h4 class="text-subtitle-1 mt-4">Submissions:</h4>
								<div v-if="assignment?.submissions?.length > 0">
									<v-list>
										<v-list-item
											v-for="submission in assignment.submissions"
											:key="submission.id"
											:title="submission.student_details?.user_details?.full_name"
											:subtitle="`Submitted: ${formatDate(submission.submitted_at)}`"
											prepend-icon="mdi-file-check-outline"
											:to="{ name: 'SubmissionDetails', params: { submissionId: submission.id }}"
											link
										/>
									</v-list>
								</div>
								<div v-else>
									<v-chip color="warning">No submissions yet</v-chip>
								</div>
							</v-card-text>
						</v-card>
					</v-col>
				</v-row>
			</v-col>
		</v-row>
	</v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getAssignment } from "../api";
import { useAuthStore } from "@/stores/auth";

const assignment = ref({});
const authStore = useAuthStore();

const props = defineProps({
	assignmentId: Number,
});

const formatDate = (dateString) => {
	return new Date(dateString).toLocaleString("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
		hour: "2-digit",
		minute: "2-digit",
		second: "2-digit",
	});
};

const fetchDetails = async () => {
	assignment.value = await getAssignment(props.assignmentId);
};

onMounted(fetchDetails);
</script>
