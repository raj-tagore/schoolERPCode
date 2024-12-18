<template>
	<div>
		<h1>
			Classes
		</h1>
	</div>
	<span>
		<ClassroomCards :classrooms="classrooms" />
	</span>
</template>

<script>
import ClassroomCards from '@/components/ClassroomCards.vue'; 
import api from '@/services/api'; // Assuming this is your axios instance

export default {
  name: 'AllClassroomsPage',
  components: {
    ClassroomCards,
  },
  data() {
    return {
      classrooms: [], 
    };
  },
  methods: {
    async getAllClassrooms() {
      try {
        const response = await api.get('/api/allocation/classrooms/all/');
        this.classrooms = response.data; // Assign the response data to classrooms
      } catch (error) {
        console.error('Error fetching classrooms:', error);
      }
    },
  },
  mounted() {
    this.getAllClassrooms(); // Fetch classrooms when the component is mounted
  },
};
</script>
