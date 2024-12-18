import axios from 'axios';
import store from '@/store';

const api = axios.create({
  baseURL: 'http://school1.localhost:8000/',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

api.interceptors.request.use(
  (config) => {
    const access = store.getters.access;
    if (access) {
      config.headers['Authorization'] = 'Bearer ' + access;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const original_request = error.config;
    if (error.response && error.response.status === 401 && !original_request._retry) {
      original_request._retry = true;
      const refresh = store.getters.refresh;
      if (refresh) {
        try {
          const response = await axios.post('http://school1.localhost:8000/api/token/refresh/', { refresh: refresh });
          store.dispatch('refreshTokens', {access: response.data.access, refresh: response.data.refresh});
          original_request.headers['Authorization'] = 'Bearer ' + response.data.access;
          return api(original_request);
        } catch (refresh_error) {
          console.error('Token refresh failed ', refresh_error);
          store.dispatch('logout');
          window.location.href = '/login';
        }
      } else {
        store.dispatch('logout');
      }
    }
    return Promise.reject(error);
  }
);

export default api;
