import { api } from "@/services/api";

const getAssignments = async (filter) =>
    (
        await api.get(
            `api/assignments/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getAssignment = async (id) =>
    (
        await api.get(
            `api/assignments/${id}`,
        )
    ).data;

export {
	getAssignments,
	getAssignment,
}
