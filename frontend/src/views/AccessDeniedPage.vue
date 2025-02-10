<template>
  <v-container class="fill-height">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6" class="text-center">
        <LottieAnimation
          :animationData="accessDeniedAnimation"
          :height="300"
          :width="400"
          :loop="true"
          :speed="1"
        />
        <h1 class="text-h3 font-weight-bold mb-4">Access Denied</h1>
        <p class="text-body-1 mb-6">
          Sorry, you don't have permission to access this page.
        </p>
        <v-btn
          color="primary"
          size="large"
          @click="$router.push({ name: 'Dashboard' })"
        >
          Back to Dashboard
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { LottieAnimation } from "lottie-web-vue"
import accessDeniedAnimation from '@/assets/access-denied.json'
</script>
