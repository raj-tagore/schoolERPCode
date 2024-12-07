<template>
<div>
    <h2>Dashboard</h2>
    <p>Welcome, {{ user.username }}!</p>
    <button @click="logoutHandler">Logout</button>
</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
computed: {
    ...mapGetters(['getUser']),
    user() {
			console.log(this.getUser);
    return this.getUser;
    },
},
methods: {
    ...mapActions(['logout']),
    async logoutHandler() {
    try {
        await this.$router.push({ name: 'Login' });
        await this.logout();
    } catch (err) {
        console.error(err);
    }
    },
},
};
</script>
  
