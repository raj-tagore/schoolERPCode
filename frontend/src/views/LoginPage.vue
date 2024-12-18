<template>
  <v-app>
    <v-container fluid class="fill-height">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <login-form
            :error="error"
            @login="handleLogin"
          ></login-form>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex';
import LoginForm from '@/components/LoginForm.vue';

export default {
  name: 'LoginPage',
  components: {
    LoginForm,
  },
  data() {
    return {
      error: '',
    };
  },
  methods: {
    ...mapActions(['login']),
    async handleLogin({ username, password }) {
      try {
        await this.login({ username, password });
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
