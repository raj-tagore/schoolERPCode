import api from "@/services/api";

const getAssignments = async (filter) =>
    (
        await api.get(
            `api/assignments/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

export {
	getAssignments
}
