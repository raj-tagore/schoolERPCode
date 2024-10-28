<template>
<div>
    <h2>Register</h2>
    <form @submit.prevent="register">
    <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required />
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required />
    </div>
    <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
    </div>
    <button type="submit">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
</div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
data() {
    return {
    username: '',
    email: '',
    password: '',
    error: '',
    };
},
methods: {
    ...mapActions(['register']),
    async register() {
    try {
        await this.register({
        username: this.username,
        email: this.email,
        password: this.password,
        });
        this.$router.push({ name: 'Login' });
    } catch (err) {
        this.error = err.response.data.detail || 'Registration failed';
    }
    },
},
};
</script>
  