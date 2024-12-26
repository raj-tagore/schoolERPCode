<template>
  <ClassroomCards />
  <v-container>
    <v-row>
      <v-col cols="12" lg="6">
        <StudentsList />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ClassroomCards from '@/components/ClassroomCards.vue';
import StudentsList from '@/components/StudentsList.vue';

export default {
  components: {
    ClassroomCards,
    StudentsList,
  }
}

</script>