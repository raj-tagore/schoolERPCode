<template>
  <ClassroomCards />
  <!-- <v-container>
    <v-row>
      <v-col cols="12" lg="6">
        <StudentsList />
      </v-col>
    </v-row>

    <TabComp :tabs="['Home', 'About', 'Contact']">
      <template #Home>
        <div>Welcome to the Home page!</div>
      </template>
      <template #About>
        <div>About us information goes here.</div>
      </template>
      <template #Contact>
        <div>Contact us at example@example.com.</div>
      </template>
    </TabComp>

  </v-container> -->
</template>

<script>
import ClassroomCards from '@/components/ClassroomCards.vue';
export default {
  components: {
    ClassroomCards,
  }
}

</script>