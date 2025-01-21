import api from "@/services/api"

const getAnnouncement = async (announcementId) => 
(await api.get(`api/announcements/${announcementId}`).data)

export { getAnnouncement };