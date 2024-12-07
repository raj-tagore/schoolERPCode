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
    SET_USER(state, userinfo) {
      state.user = userinfo.user;
      state.user_type = userinfo.type;
    },
    SET_TOKENS(state, tokens) {
      state.access = tokens.access;
      state.refresh = tokens.refresh;
      Cookies.set('access', tokens.access);
      Cookies.set('refresh', tokens.refresh);
    },
    CLEAR_AUTH(state) {
      state.user = null;
      state.user_type = null;
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
        commit('SET_TOKENS', {access:response.data.access, refresh:response.data.refresh});
        
        // set user
        const user_id = response.data.user_id;
        const user_type = response.data.type;
        let user_fetch_url = `api/accounts/${user_id}/`;
        if (user_type == "internal") {
          user_fetch_url = `api/accounts/users/${user_id}/`;
        }
        const user_response = await api.get(user_fetch_url);
        commit('SET_USER', {user:user_response.data, type:user_type});

      } catch (error) {
        console.error('Login failed: ', error);
      }
    },
    logout({ commit }) {
      commit('CLEAR_AUTH');
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
