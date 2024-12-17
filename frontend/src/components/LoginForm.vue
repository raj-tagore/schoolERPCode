<template>
    <v-card class="pa-4">
      <v-card-title class="headline justify-center">Login</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="onSubmit">
          <v-text-field
            v-model="localUsername"
            label="Username"
            required
            prepend-icon="mdi-account"
            outlined
          ></v-text-field>
          <v-text-field
            v-model="localPassword"
            label="Password"
            type="password"
            required
            prepend-icon="mdi-lock"
            outlined
          ></v-text-field>
  
          <v-btn color="primary" class="mt-4" block type="submit">
            Login
          </v-btn>
  
          <v-alert v-if="error" type="error" class="mt-3" dense border="left">
            {{ error }}
          </v-alert>
        </v-form>
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    name: 'LoginForm',
    props: {
      error: {
        type: String,
        default: '',
      },
    },
    data() {
      return {
        localUsername: '',
        localPassword: '',
      };
    },
    methods: {
      onSubmit() {
        // Emit an event carrying the username and password back to the parent
        this.$emit('login', {
          username: this.localUsername,
          password: this.localPassword,
        });
      },
    },
  };
  </script>
  