import { api } from "@/services/api";

const getAssignments = async (filter) =>
    (
        await api.get("api/assignments/all", {
            params: { ...filter },
        })
    ).data;

const getAssignment = async (id) =>
    (await api.get(`api/assignments/${id}`)).data;

const updateAssignment = async (assignment) =>
    await api.put(`api/assignments/${assignment.id}/`, assignment);

const createAssignment = async (data) =>
    await api.post("api/assignments/create/", data);

export { getAssignments, getAssignment, updateAssignment, createAssignment };
