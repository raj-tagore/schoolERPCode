import { api } from "@/services/api";

const getAnnouncements = async (filter) =>
    (
        await api.get(
            `api/announcements/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data.results;

const getAnnouncement = async (id) => {
    try {
        const response = await api.get(`api/announcements/${id}`);
        return response.data;
    } catch (error) {
        console.error('Failed to fetch announcement:', error);
        throw error;
    }
};

const updateAnnouncement = async (id, data) => {
    try {
        const response = await api.put(`api/announcements/${id}/`, data);
        return { success: true, data: response.data };
    } catch (error) {
        console.error('Failed to update announcement:', error);
        return { 
            success: false, 
            error: error.response?.data || 'Failed to update announcement'
        };
    }
};

export { getAnnouncements, getAnnouncement, updateAnnouncement };
