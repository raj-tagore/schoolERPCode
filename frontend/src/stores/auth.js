import { defineStore } from 'pinia'
import api from '@/services/api'
import Cookies from 'js-cookie'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: 'guest',
    access: null,
    refresh: null,
  }),

  getters: {
    isAuth: (state) => !!state.access,
    getUser: (state) => state.user,
    getAccess: (state) => state.access,
    getRefresh: (state) => state.refresh,
  },

  actions: {
    async login(credentials) {
      const response = await api.post('api/token/', credentials)
      this.setTokens({ access: response.data.access, refresh: response.data.refresh })

      const userResponse = await api.get('/api/accounts/self/')
      this.setUser(userResponse.data)
    },

    async register(profile) {
      const resp = await api.post('api/accounts/', profile)
      if (!resp || resp.status !== 201) {
        throw new Error("Registration failed")
      }
      return true
    },

    logout() {
      this.clearAuth()
    },

    refreshTokens(tokens) {
      this.setTokens(tokens)
    },

    // Utility actions to manage state and cookies
    setTokens({ access, refresh }) {
      this.access = access
      this.refresh = refresh
      Cookies.set('access', access)
      Cookies.set('refresh', refresh)
    },

    setUser(userInfo) {
      this.user = userInfo
    },

    clearAuth() {
      this.user = 'guest'
      this.access = null
      this.refresh = null
      Cookies.remove('access')
      Cookies.remove('refresh')
    }
  },

  // Persisting specified parts of the state
  persist: {
    paths: ['access', 'refresh', 'user'],
  },
})
