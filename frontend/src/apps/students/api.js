import { api } from "@/services/api";

const getStudents = async (filter) =>
    (
        await api.get("api/accounts/students/all", {
            params: { page_size: 10000, ...filter },
        })
    ).data;

const getStudent = async (id) =>
    (await api.get(`api/accounts/students/${id}`)).data;

const updateStudent = async (student) =>
    await api.put(`api/accounts/students/${student.id}/`, student);

const getStudentInfoFromObj = (item) => ({
    title: `${item.user_details.full_name}`,
    subtitle: item.identifier,
    value: item.id,
});

const getStudentStats = async () =>
    (await api.get("api/accounts/students/stats/")).data;

export {
    getStudents,
    getStudent,
    getStudentInfoFromObj,
    updateStudent,
    getStudentStats,
};
