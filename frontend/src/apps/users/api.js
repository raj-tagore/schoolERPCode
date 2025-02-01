import { api } from "@/services/api";

const getUser = async (id) => (await api.get(`api/users/${id}`)).data;

const updateUser = async (user) => await api.put(`api/users/${user.id}/`, user);

export {
    getUser,
    updateUser,
};
