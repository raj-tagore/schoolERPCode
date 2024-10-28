<template>
<div>
    <h2>Login</h2>
    <form @submit.prevent="login">
    <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required />
    </div>
    <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
    </div>
    <button type="submit">Login</button>
    </form>
    <p v-if="error">{{ error }}</p>
</div>
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
    async login() {
    try {
        await this.login({
        username: this.username,
        password: this.password,
        });
        this.$router.push({ name: 'Dashboard' });
    } catch (err) {
        this.error = err.response.data.detail || 'Login failed';
    }
    },
},
};
</script>
  