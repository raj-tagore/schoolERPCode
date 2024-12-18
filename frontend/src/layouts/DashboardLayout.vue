<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" color="grey lighten-4">
      <v-list dense>
        <!-- User Info -->
        <v-list-item>
          <div>
            <h3>{{ user.first_name }} {{ user.last_name }}</h3>
            <h4>{{ user.username }}</h4>
            <span>User Role to be here</span>
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
            <v-list-item to="/announcement">
              <v-list-item-title>View Announcements</v-list-item-title>
            </v-list-item>
            <v-list-item to="/announcement/create">
              <v-list-item-title>Create Announcement</v-list-item-title>
            </v-list-item>
          </v-list>
        </ExpandableListItem>
        <ExpandableListItem title="Classrooms">
          <v-list dense>
            <v-list-item to="/classroom">
              <v-list-item-title>View Classrooms</v-list-item-title>
            </v-list-item>
            <v-list-item to="/classroom/create">
              <v-list-item-title>Create Classroom</v-list-item-title>
            </v-list-item>
          </v-list>
        </ExpandableListItem>
        <ExpandableListItem title="Subjects">
          <v-list dense>
            <v-list-item to="/subject">
              <v-list-item-title>View Subjects</v-list-item-title>
            </v-list-item>
            <v-list-item to="/subject/create">
              <v-list-item-title>Create Subject</v-list-item-title>
            </v-list-item>
          </v-list>
        </ExpandableListItem>
        <ExpandableListItem title="Assessments">
          <v-list dense>
            <v-list-item to="/assessment">
              <v-list-item-title>View Assessments</v-list-item-title>
            </v-list-item>
            <v-list-item to="/assessment/create">
              <v-list-item-title>Create Assessment</v-list-item-title>
            </v-list-item>
          </v-list>
        </ExpandableListItem>
        <ExpandableListItem title="Assignments">
          <v-list dense>
            <v-list-item to="/assignment">
              <v-list-item-title>View Assignments</v-list-item-title>
            </v-list-item>
            <v-list-item to="/assignment/create">
              <v-list-item-title>Create Assignment</v-list-item-title>
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
