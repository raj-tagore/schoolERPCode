import { createStore } from 'vuex';
import api from '../services/api';
import Cookies from 'js-cookie';

export default createStore({
  state: {
    user: null,
    accessToken: Cookies.get('access_token') || '',
    refreshToken: Cookies.get('refresh_token') || '',
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    CLEAR_AUTH(state) {
      state.user = null;
      Cookies.remove('access_token');
      Cookies.remove('refresh_token');
    },
  },
  actions: {
    async login({ commit }, credentials) {
      const response = await api.post('token/', credentials);
      const user_id = response.data.user_id;
      const user = await api.get(`api/accounts/${user_id}/`);
      console.log(user);
      commit('SET_USER', user);
    },
  },
  getters: {
    isAuthenticated: state => !!state.accessToken,
    getUser: state => state.user,
  },
  modules: {},
});
