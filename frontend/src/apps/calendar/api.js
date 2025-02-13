import { api } from "@/services/api";

const getCalendars = async (filter) =>
    (
        await api.get("api/calendars/all", {
            params: { ...filter },
        })
    ).data;

const getCalendar = async (id) =>
    (await api.get(`api/calendars/${id}`)).data;

const updateCalendar = async (calendar) =>
    await api.put(`api/calendars/${calendar.id}/`, calendar);

const createCalendar = async (data) =>
    await api.post("api/calendars/create/", data);

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
    getCalendars,
    getCalendar,
    updateCalendar,
    createCalendar,
    getEvents,
    getEvent,
    updateEvent,
    createEvent,
};
