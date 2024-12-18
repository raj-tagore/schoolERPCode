<template>
    <v-card class="mb-4">
        <v-card-title>{{ title }}</v-card-title>
        <v-card-subtitle v-if="subtitle">{{ subtitle }}</v-card-subtitle>
        <v-card-text>
        <slot name="content"></slot>
        </v-card-text>
    </v-card>
</template>
  
<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    subtitle: {
      type: String,
      default: ''
    }
  }
}
</script>
  
<style scoped>
</style>
