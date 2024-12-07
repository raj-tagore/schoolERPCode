<template>
<form>
    <h2>Register</h2>
    <form @submit.prevent="registerHandler">
    <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required />
    </div>
    <div>
        <label for="name">Name:</label>
        <input type="text" v-model="name" required />
    </div>
    <div>
        <label for="address">Address:</label>
        <input type="text" v-model="address" required />
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required />
    </div>
    <div>
        <label for="phone">Phone:</label>
        <input type="tel" v-model="phone" required />
    </div>
    <div>
        <label for="whatsapp">Whatsapp Number:</label>
        <input type="tel" v-model="whatsapp" required />
    </div>
    <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
    </div>
    <button type="submit">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
</form>
</template>

<script>
import { mapActions } from 'vuex';

export default {
data() {
    return {
    username: '',
	first_name: '',
	last_name: '',
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
        if (await this.register({
        username: this.username,
		first_name: this.name.split(' ')[0],
		last_name: this.name.split(' ')[1],
		address: this.address,
		phone: this.phone,
		whatsapp: this.whatsapp,
        email: this.email,
        password: this.password,
		})) {
			alert('Registration successful');
		}
    } catch (err) {
        this.error = err.response.data.detail || 'Registration failed';
    }
    },
},
};
</script>
  
