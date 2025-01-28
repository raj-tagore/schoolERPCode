import api from "@/services/api";

const getAssignments = async (filter) =>
    (await api.get(`api/assignments/all`, { params: filter })).data;

const getAssignment = async (id) =>
    (await api.get(`api/assignments/${id}`)).data;

const updateAssignment = async (id, data) =>
    await api.put(`api/assignments/${id}/`, data);

export { getAssignments, getAssignment, updateAssignment };
