import { api } from "@/services/api";

const getAssignmentsListing = async (filter) =>
    (await api.get("api/assignments/all", { params: filter })).data;

const getAssignments = async (filter) =>
    (await getAssignmentsListing({page_size: 10000, ...filter})).results;

const getAssignment = async (id) =>
    (await api.get(`api/assignments/${id}`)).data;

const updateAssignment = async (id, data) =>
    await api.put(`api/assignments/${id}/`, data);

export {
    getAssignments,
    getAssignmentsListing,
    getAssignment,
    updateAssignment,
};
