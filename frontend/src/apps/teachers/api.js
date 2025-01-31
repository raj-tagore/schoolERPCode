import { api } from "@/services/api";

const getTeachers = async (filter) =>
    (
        await api.get("api/accounts/teachers/all", {
            params: { page_size: 10000, ...filter },
        })
    ).data;

const getTeacher = async (id) =>
    (await api.get(`api/accounts/teachers/${id}`)).data;


const getTeacherInfoFromObj = (item) => ({
    title: `${item.user_details.full_name}`,
    subtitle: item.identifier,
    value: item.id,
});


const getTeacherStats = async () =>
    (await api.get("api/accounts/teachers/stats/")).data;

export {
    getTeachers,
    getTeacher,
    getTeacherInfoFromObj,
    getTeacherStats,
};
