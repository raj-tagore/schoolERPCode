import { createStore } from 'vuex';
import api from '../services/api';
import Cookies from 'js-cookie';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
  state: {
    user: null,
    user_type: null,
    access: null,
    refresh: null,
  },
  
  // synchronous functions to modify state
  mutations: {
    SET_USER(state, user, type) {
      state.user = user;
      state.user_type = type;
    },
    SET_TOKENS(state, access, refresh) {
      state.access = access;
      state.refresh = refresh;
      Cookies.set('access', access);
      Cookies.set('refresh', refresh);
    },
    CLEAR_AUTH(state) {
      state.user = null;
      state.access = null;
      state.refresh = null;
      Cookies.remove('access');
      Cookies.remove('refresh');
    }
  },

  // async functions to do mutations
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await api.post('token/', credentials);

        // set tokens
        commit('SET_TOKENS', response.data.access, response.data.refresh);
        
        // set user
        const user_id = response.data.user_id;
        const user_type = response.data.type;
        let user_fetch_url = `api/accounts/${user_id}/`;
        if (user_type == "internal") {
          user_fetch_url = `api/accounts/users/${user_id}/`;
        }
        const user_response = await api.get(user_fetch_url);
        const user = user_response.data;
        commit('SET_USER', user, user_type);

      } catch (error) {
        console.error('Login failed: ', error);
      }
    },
    logout({ commit }) {
      commit('CLEAR_AUTH');
      window.location.href = '/login';
    },
    refreshTokens({ commit }, access, refresh) {
      commit('SET_TOKENS', access, refresh);
    }
  },

  // computations on state
  getters: {
    isAuth: state => !!state.access,
    getUser: state => state.user,
    getUserType: state => state.user_type,
    access: state => state.access,
    refresh: state => state.refresh,
  },
  plugins: [createPersistedState()],
})
