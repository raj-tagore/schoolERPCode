import { defineStore } from 'pinia'
import { api } from '@/services/api'
import Cookies from 'js-cookie'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: 'guest',
    access: null,
    refresh: null,
    account: null,
  }),

  getters: {
    isAuth: (state) => !!state.access,
    getUser: (state) => state.user,
    getAccess: (state) => state.access,
    getRefresh: (state) => state.refresh,
    hasPermission: (state) => (permission) => {
      return state.account?.group_details?.permissions.some(
        perm => perm.codename === permission
      ) || false
    },
  },

  actions: {
    async login(credentials) {
      // First get tokens
      const response = await api.post('api/token/', credentials)
      this.setTokens({ access: response.data.access, refresh: response.data.refresh })

      // Then get user data
      const userResponse = await api.get('/api/users/self/')
      this.setUser(userResponse.data)

      // If user has an account, fetch its details including permissions
      if (userResponse.data.account) {
        await this.setActiveAccount(userResponse.data.account)
      }
    },

    async setActiveAccount(accountInfo) {
      const { type, id } = accountInfo
      // Fetch account details including permissions
      const accountResponse = await api.get(`/api/accounts/${type.toLowerCase()}s/${id}/`)
      this.account = accountResponse.data
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
      this.account = null
      Cookies.remove('access')
      Cookies.remove('refresh')
    },

    logout() {
      this.clearAuth()
    }
  },

  // Persisting specified parts of the state
  persist: {
    paths: ['access', 'refresh', 'user', 'account'],
  },
})
