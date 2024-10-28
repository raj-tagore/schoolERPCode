import { createStore } from 'vuex';
import api from '../services/api';

export default createStore({
  state: {
    user: null,
    accessToken: localStorage.getItem('access_token') || '',
    refreshToken: localStorage.getItem('refresh_token') || '',
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    SET_TOKENS(state, tokens) {
      state.accessToken = tokens.access;
      state.refreshToken = tokens.refresh;
    },
    CLEAR_AUTH(state) {
      state.user = null;
      state.accessToken = '';
      state.refreshToken = '';
    },
  },
  actions: {
    async register({ commit }, userData) {
        const response = await api.post('users/register/', userData);
        commit('SET_USER', response.data);
        return response.data;
    },
    async login({ commit }, credentials) {
        const response = await api.post('users/login/', credentials);
        const tokens = response.data;
        localStorage.setItem('access_token', tokens.access);
        localStorage.setItem('refresh_token', tokens.refresh);
        commit('SET_TOKENS', tokens);
        // Optionally fetch user profile
        const userResponse = await api.get('users/profile/');
        commit('SET_USER', userResponse.data);
        return userResponse.data;
    },
    async logout({ commit }) {
        await api.post('users/logout/', { refresh: localStorage.getItem('refresh_token') });
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        commit('CLEAR_AUTH');
    },
    async fetchUser({ commit }) {
        const response = await api.get('users/profile/');
        commit('SET_USER', response.data);
    },
  },
  getters: {
    isAuthenticated: state => !!state.accessToken,
    getUser: state => state.user,
  },
  modules: {},
});
