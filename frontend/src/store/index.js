import { createStore } from 'vuex';
import api from '@/services/api';
import Cookies from 'js-cookie';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
  state: {
    user: "guest",
    access: null,
    refresh: null,
  },
  mutations: {
    SET_USER(state, userinfo) {
      state.user = userinfo.user;
    },
    SET_TOKENS(state, tokens) {
      state.access = tokens.access;
      state.refresh = tokens.refresh;
      Cookies.set('access', tokens.access);
      Cookies.set('refresh', tokens.refresh);
    },
    CLEAR_AUTH(state) {
      state.user = "guest";
      state.access = null;
      state.refresh = null;
      Cookies.remove('access');
      Cookies.remove('refresh');
    }
  },
  actions: {
    async login({ commit }, credentials) {
      const response = await api.post('api/token/', credentials);
      commit('SET_TOKENS', { access: response.data.access, refresh: response.data.refresh });

      const user_response = await api.get('/api/accounts/self/');
      commit('SET_USER', { user: user_response.data});
    },
    async register(_, profile) {
      const resp = await api.post('api/accounts/', profile);
      if (!resp || resp.status !== 201) {
        throw new Error("Registration failed");
      }
      return true;
    },
    logout({ commit }) {
      commit('CLEAR_AUTH');
    },
    refreshTokens({ commit }, tokens) {
      commit('SET_TOKENS', tokens);
    },
  },
  getters: {
    isAuth: state => !!state.access,
    getUser: state => state.user,
    access: state => state.access,
    refresh: state => state.refresh,
  },
  plugins: [createPersistedState({
    paths: ['access', 'refresh', 'user'],
  })],
});
