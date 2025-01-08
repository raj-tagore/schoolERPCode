<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" color="grey lighten-4">
      <v-list dense>
        <!-- User Info -->
        <v-list-item>
          <v-card prepend-icon="mdi-account" class="pa-2 ma-2" 
          :title="user.first_name + ' ' + user.last_name"
          :subtitle="user.account?.type || 'No linked account'">
          <v-card-actions>
            <v-btn @click="logoutHandler">Logout</v-btn>
          </v-card-actions>
          </v-card>
        </v-list-item>

        <v-divider :thickness="10" class="border-opacity-100"></v-divider>

        <!-- Dashboard -->
        <v-list-item :to="{name: 'Dashboard'}">
          <v-list-item-title>Dashboard</v-list-item-title>
        </v-list-item>

        <v-list-item :to="{name: 'Classrooms'}">
          <v-list-item-title>Classes</v-list-item-title>
        </v-list-item>
        
        <!-- <ExpandableListItem title="Classrooms">
          <v-list dense>
            <v-list-item to="/classrooms">
              <v-list-item-title>View Classrooms</v-list-item-title>
            </v-list-item>
            <v-list-item to="/classrooms/create">
              <v-list-item-title>Create Classroom</v-list-item-title>
            </v-list-item>
          </v-list>
        </ExpandableListItem> -->

      </v-list>
    </v-navigation-drawer>


    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>School ERP Dashboard</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="logoutHandler">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth' // Pinia store
// import ExpandableListItem from '@/components/c-expandable-list-item.vue'

const drawer = ref(false)

const router = useRouter()
const authStore = useAuthStore()

const user = computed(() => authStore.user)

// Actions
function logoutHandler() {
  router.push({ name: 'Login' })
  authStore.logout()
}
</script>

<script>
// For Options API style components, remove this block entirely since we are using the <script setup> syntax above.
// This block is intentionally left empty as all logic is now in <script setup>.
</script>

<style>
/* Add any custom styles if necessary */
</style>
