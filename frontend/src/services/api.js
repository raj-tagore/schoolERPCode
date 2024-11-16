import axios from 'axios';
import Cookies from 'js-cookie';

const api = axios.create({
  baseURL: 'http://school1.localhost:8000/',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response && error.response.status === 401 && Cookies.get('refresh_token')) {
      try {
        await axios.post('token/refresh/', {
          refresh: Cookies.get('refresh_token'),
        });
        return axios(error.config); // Retry the original request
      } catch (refreshError) {
        console.error('Token refresh failed', refreshError);
        Cookies.remove('access_token');
        Cookies.remove('refresh_token');
        // Redirect to login page or handle logout
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export default api;