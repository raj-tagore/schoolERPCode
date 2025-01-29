import { api } from "@/services/api";

const getAnnouncementsPaginated = async (filter) =>
    (await api.get("api/announcements/all", { params: filter })).data;

const getAnnouncements = async (filter) =>
    (await getAnnouncementsPaginated({ page_size: 10000, ...filter })).results;

const getAnnouncement = async (id) =>
    (await api.get(`api/announcements/${id}`)).data;

const updateAnnouncement = async (id, data) =>
    await api.put(`api/announcements/${id}/`, data);

export {
    getAnnouncements,
    getAnnouncementsPaginated,
    getAnnouncement,
    updateAnnouncement,
};
