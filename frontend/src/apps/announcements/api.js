import { api } from "@/services/api";

const getAnnouncements = async (filter) =>
    (await api.get("api/announcements/all", { params: filter })).data;

const getAnnouncement = async (id) =>
    (await api.get(`api/announcements/${id}`)).data;

const updateAnnouncement = async (id, data) =>
    await api.put(`api/announcements/${id}/`, data);

export { getAnnouncements, getAnnouncement, updateAnnouncement };
