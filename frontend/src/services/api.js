import axios from 'axios';
import store from '@/store';

const api = axios.create({
  baseURL: 'http://school1.localhost:8000/',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// request interceptor to add access
api.interceptors.request.use(
  (config) => {
    const access = store.getters.access;
    if (access) {
      config.headers['authorization'] = 'Bearer ' + access;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// response interceptor to set access and refresh tokens
api.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const original_request = error.config;

    // if 401 and not refreshed tokens
    if (
      error.response && 
      error.response.status === 401 && 
      !original_request._retry
    ) {
      original_request._retry = true;
      const refresh = store.getters.refresh;
      if (refresh) {
        // refresh token is available
        try {
          const response = await axios.post('token/refresh', {refresh: refresh,});
          store.dispatch('refreshTokens', response.data.access, response.data.refresh);
          original_request.headers['Authorization'] = 'Bearer ' + response.data.access;
          return api(original_request);
        } catch (refresh_error) {
          // logout and remove tokens if refresh fails
          console.error('Token refresh failed ', refresh_error);
          store.dispatch('logout');
          window.location.href = '/login';
        }
      } else {
        // refresh token was not available or valid
        store.dispatch('logout');
      }
    }

    return Promise.reject(error);
  }
);

export default api;