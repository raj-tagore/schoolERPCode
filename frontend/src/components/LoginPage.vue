<template>
    <v-app>
      <v-container fluid class="fill-height">
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="pa-4">
              <v-card-title class="headline justify-center">Login</v-card-title>
              <v-card-text>
                <v-form @submit.prevent="handleLogin">
                  <v-text-field
                    v-model="username"
                    label="Username"
                    required
                    prepend-icon="mdi-account"
                    outlined
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
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
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  
  export default {
    name: 'LoginPage',
    data() {
      return {
        username: '',
        password: '',
        error: '',
      };
    },
    methods: {
      ...mapActions(['login']),
      async handleLogin() {
        try {
          await this.login({ username: this.username, password: this.password });
          this.$router.push({ name: 'Dashboard' });
        } catch (err) {
          this.error = 'Login failed. Please check your credentials.';
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .fill-height {
    height: 100vh;
  }
  </style>
  