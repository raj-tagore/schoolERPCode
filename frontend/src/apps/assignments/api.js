import { api } from "@/services/api";

const getAssignments = async (filter) =>
    (
        await api.get("api/assignments/all", {
            params: { page_size: 10000, ...filter },
        })
    ).data;

const getAssignment = async (id) =>
    (await api.get(`api/assignments/${id}`)).data;

const updateAssignment = async (id, data) =>
    await api.put(`api/assignments/${id}/`, data);

const createAssignment = async (data) =>
    await api.post("api/assignments/create/", data);

export { getAssignments, getAssignment, updateAssignment, createAssignment };
