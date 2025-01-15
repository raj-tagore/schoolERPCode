import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const api = axios.create({
    baseURL: "http://school1.localhost:8000/",
    headers: {
        "Content-Type": "application/json",
    },
    withCredentials: true,
});

api.interceptors.request.use(
    (config) => {
        const authStore = useAuthStore();
        const access = authStore.getAccess;
        if (access) {
            config.headers["Authorization"] = "Bearer " + access;
        }
        return config;
    },
    (error) => Promise.reject(error),
);

api.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        const authStore = useAuthStore();
        const original_request = error.config;
        if (
            error.response &&
            error.response.status === 401 &&
            !original_request._retry
        ) {
            original_request._retry = true;
            const refresh = authStore.getRefresh;
            if (refresh) {
                try {
                    const response = await axios.post(
                        "http://school1.localhost:8000/api/token/refresh/",
                        { refresh: refresh },
                    );
                    authStore.refreshTokens({
                        access: response.data.access,
                        refresh: response.data.refresh,
                    });
                    original_request.headers["Authorization"] =
                        "Bearer " + response.data.access;
                    return api(original_request);
                } catch (refresh_error) {
                    console.error("Token refresh failed ", refresh_error);
                    authStore.logout();
                    window.location.href = "/login";
                }
            } else {
                authStore.logout();
            }
        }
        return Promise.reject(error);
    },
);

export default api;
