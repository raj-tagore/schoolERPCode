<template>
	<hgroup>
		<h1>Dashboard</h1>
		<p>Welcome, {{ user.username }}!</p>
	</hgroup>
	<div class="grid">
		<button class="extra_padding" @click="logoutHandler">Logout</button>
		<a href="/register">Create User</a>
	</div>
</template>

<style>
.extra_padding {
	padding: 10px;
}
</style>

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
  
