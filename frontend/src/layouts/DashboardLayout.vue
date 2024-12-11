<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" color="grey lighten-4">
      <v-list dense>
        <!-- User Info -->
        <v-list-item>
          <div>
            <h3>{{ user.first_name }} {{ user.last_name }}</h3>
            <h4>{{ user.username }}</h4>
            <span>{{ userType }}</span>
          </div>
        </v-list-item>

        <v-divider :thickness="10" class="border-opacity-100"></v-divider>

        <!-- Dashboard -->
        <v-list-item to="/dashboard">
          <v-list-item-title>Dashboard</v-list-item-title>
        </v-list-item>

        <!-- Create User -->
        <v-list-item to="/register">
          <v-list-item-title>Create User</v-list-item-title>
        </v-list-item>

        <!-- Announcements Toggle -->
        <v-list-item @click="announcementsOpen = !announcementsOpen" class="cursor-pointer">
          <v-list-item-title>Announcements</v-list-item-title>
          <v-spacer></v-spacer>
          <v-icon>{{ announcementsOpen ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
        </v-list-item>

        <!-- Nested Items (Shown/Hidden with v-expand-transition) -->
        <v-expand-transition>
          <div v-if="announcementsOpen" style="padding-left: 24px;">
            <v-list-item to="/announcement">
              <v-list-item-title>View Announcements</v-list-item-title>
            </v-list-item>
            <v-list-item to="/announcement/create">
              <v-list-item-title>Create Announcement</v-list-item-title>
            </v-list-item>
          </div>
        </v-expand-transition>

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
      <v-container class="mt-5">
        <!-- Renders the page component inside the main layout -->
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      drawer: false,
      announcementsOpen: false,
    };
  },
  methods: {
    ...mapActions(['logout']),
    logoutHandler() {
      this.$router.push({ name: 'Login' });
      this.logout();
    },
  },
  computed: {
    ...mapGetters(['getUser', 'getUserType']),
    user() {
      return this.getUser;
    },
    userType() {
      return this.getUserType;
    },
  },
};
</script>
