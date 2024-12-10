<template>
    <v-app>
      <v-main>
        <v-container>
          <h2>Register</h2>
          <v-form @submit.prevent="registerHandler">
            <v-text-field v-model="username" label="Username" required outlined></v-text-field>
            <v-text-field v-model="name" label="Name" required outlined></v-text-field>
            <v-text-field v-model="address" label="Address" required outlined></v-text-field>
            <v-text-field v-model="email" label="Email" required outlined></v-text-field>
            <v-text-field v-model="phone" label="Phone" required outlined></v-text-field>
            <v-text-field v-model="whatsapp" label="WhatsApp Number" required outlined></v-text-field>
            <v-text-field v-model="password" label="Password" type="password" required outlined></v-text-field>
            
            <v-btn color="primary" type="submit" class="mt-4">Register</v-btn>
          </v-form>
          <v-alert v-if="error" type="error" class="mt-3" dense border="left">
            {{ error }}
          </v-alert>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  
  export default {
    data() {
      return {
        username: '',
        name: '',
        address: '',
        phone: '',
        whatsapp: '',
        email: '',
        password: '',
        error: '',
      };
    },
    methods: {
      ...mapActions(['register']),
      async registerHandler() {
        try {
          const result = await this.register({
            username: this.username,
            first_name: this.name.split(' ')[0] || '',
            last_name: this.name.split(' ')[1] || '',
            address: this.address,
            phone: this.phone,
            whatsapp: this.whatsapp,
            email: this.email,
            password: this.password,
          });
          if (result) {
            alert('Registration successful');
            this.$router.push({ name: 'Dashboard' });
          }
        } catch (err) {
          this.error = (err.response && err.response.data.detail) || 'Registration failed';
        }
      },
    },
  };
  </script>
  