<template>
  <v-container>
    <v-row class="ma-2">
      <v-col cols="12">
        <ParentCard :parent="parent" v-if="parent?.user_details" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getParent } from "@/apps/parents/api";
import ParentCard from "@/apps/parents/components/ParentCard";

const parent = ref({});

const props = defineProps({
  parentId: Number,
});

const fetchDetails = async () => {
  parent.value = await getParent(props.parentId);
};

onMounted(fetchDetails);
</script>
