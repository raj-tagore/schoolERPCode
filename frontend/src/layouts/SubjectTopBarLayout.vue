<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Subjects</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <v-container class="mt-5">
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>


<script>
// For Options API style components, remove this block entirely since we are using the <script setup> syntax above.
// This block is intentionally left empty as all logic is now in <script setup>.
</script>

<style>
/* Add any custom styles if necessary */
</style>
