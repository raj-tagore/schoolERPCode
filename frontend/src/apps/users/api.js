import { api } from "@/services/api";

const getTeachers = async (filter) =>
    (await api.get("api/accounts/teachers/all", { params: { page_size: 10000, ...filter } })).data;

const getTeacher = async (id) =>
    (await api.get(`api/accounts/teachers/${id}`)).data;

const getStudents = async (filter) =>
    (await api.get("api/accounts/students/all", { params: { filter } })).data;

const getStudent = async (id) =>
    (await api.get(`api/accounts/students/${id}`)).data;

const getParents = async (filter) =>
    (await api.get("api/accounts/parents/all", { params: { filter } })).data;

const getParent = async (id) =>
    (await api.get(`api/accounts/parents/${id}`)).data;

const getUser = async (id) => (await api.get(`api/users/${id}`)).data;

const updateStudent = async (student) =>
    await api.put(`api/accounts/students/${student.id}/`, student);

const updateUser = async (user) => await api.put(`api/users/${user.id}/`, user);

const getTeacherInfoFromObj = (item) => ({
    title: `${item.user_details.full_name}`,
    subtitle: item.identifier,
    value: item.id,
});

const getStudentInfoFromObj = (item) => ({
    title: `${item.user_details.full_name}`,
    subtitle: item.identifier,
    value: item.id,
});

const getStudentStats = async () =>
    (await api.get("api/accounts/students/stats/")).data;

export {
    getTeachers,
    getTeacher,
    getStudents,
    getStudent,
    getParents,
    getParent,
    getUser,
    getTeacherInfoFromObj,
    getStudentInfoFromObj,
    updateStudent,
    updateUser,
    getStudentStats,
};
