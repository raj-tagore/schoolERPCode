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
        <ExpandableListItem title="Announcements">
          <v-list dense>
            <v-list-item to="/announcements">
              <v-list-item-title>View Announcements</v-list-item-title>
            </v-list-item>
            <v-list-item to="/announcements/create">
              <v-list-item-title>Create Announcement</v-list-item-title>
            </v-list-item>
          </v-list>
        </ExpandableListItem>


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

import ExpandableListItem from '@/components/c-expandable-list-item.vue';

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
  components: {
	ExpandableListItem,
  },
};
</script>
