<template>
<v-container>
  <v-row>
    <v-col cols="12" lg="4">
      <SubjectCards />
    </v-col>
  </v-row>
</v-container>
</template>

<script>
import SubjectCards from '@/components/SubjectCards.vue';

export default {
  components: {
    SubjectCards,
  },
  props: ['id'],
}
</script>