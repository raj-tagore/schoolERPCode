import api from "@/services/api";

const getSubjects = async (filter) => 
    (
        await api.get(
            `api/allocation/subjects/all/${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

export { getSubjects };
