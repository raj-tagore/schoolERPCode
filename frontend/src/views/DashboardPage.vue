<template>
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {{ user.username }}!</p>
    </div>
  </template>
  
  <script>
  import { mapGetters } from 'vuex';
  
  export default {
    computed: {
      ...mapGetters(['getUser']),
      user() {
        return this.getUser;
      },
    },
  };
  </script>
  