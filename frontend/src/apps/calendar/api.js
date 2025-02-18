import { api } from "@/services/api";

const getEvents = async (filter) =>
    (
        await api.get("api/events/all", {
            params: { ...filter },
        })
    ).data;

const getEvent = async (id) =>
    (await api.get(`api/events/${id}`)).data;

const updateEvent = async (event) =>
    await api.put(`api/events/${event.id}/`, event);

const createEvent = async (data) =>
    await api.post("api/events/create/", data);

export {
    getEvents,
    getEvent,
    updateEvent,
    createEvent,
};
