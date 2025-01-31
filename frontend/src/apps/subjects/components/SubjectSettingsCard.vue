<template>
  <FormCard 
    title="Subject Settings"
    :onSubmit="handleUpdate"
  >
    <v-row v-if="subject">
      <v-col>
        <v-text-field 
          label="Name" 
          v-model="subject.name"
          density="comfortable"
        ></v-text-field>
        <v-textarea 
          label="Description" 
          v-model="subject.description"
          density="comfortable"
        ></v-textarea>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-autocomplete 
          v-if="teachers.length>0" 
          label="Teacher" 
          :item-props="teacherInfoFromObj" 
          :items="teachers" 
          v-model="subject.teacher"
          density="comfortable"
        ></v-autocomplete>
      </v-col>
      <v-col>
        <v-checkbox 
          label="Is Active" 
          v-model="subject.is_active"
          density="comfortable"
        ></v-checkbox>
      </v-col>
    </v-row>
  </FormCard>
</template>
  
<script setup>
import { ref, onMounted } from "vue";
import { getTeachers } from "@/apps/users/api";
import { updateSubject } from "@/apps/subjects/api";
import FormCard from "@/components/FormCard.vue";

const props = defineProps(["subject"]);
const teachers = ref([]);

const teacherInfoFromObj = (item) => ({
	title: `${item.user.full_name}`,
	subtitle: item.identifier,
	value: item.id,
});

const handleUpdate = async () => {
	try {
		await updateSubject(props.subject);
		return { success: true };
	} catch (error) {
		console.error("Failed to update subject:", error);
		return { success: false, error };
	}
};

onMounted(async () => {
	teachers.value = (await getTeachers()).results;
});
</script>
  
