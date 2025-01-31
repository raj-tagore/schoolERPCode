import { api } from "@/services/api";

const getParents = async (filter) =>
    (
        await api.get("api/accounts/parents/all", {
            params: { page_size: 10000, ...filter },
        })
    ).data;

const getParent = async (id) =>
    (await api.get(`api/accounts/parents/${id}`)).data;

const getTeacherStats = async () =>
    (await api.get("api/accounts/teachers/stats/")).data;

export { getParents, getParent, getTeacherStats };
