import { api } from "@/services/api";

const getTeachersPaginated = async (filter) =>
    (await api.get("api/accounts/teachers/all", { params: filter })).data;

const getTeachers = async (filter) =>
    (await getTeachersPaginated({ page_size: 10000, ...filter })).results;

const getTeacher = async (id) =>
    (await api.get(`api/accounts/teachers/${id}`)).data;

const getStudentsPaginated = async (filter) =>
    (await api.get("api/accounts/students/all", { params: filter })).data;

const getStudents = async (filter) =>
    (await getStudentsPaginated({ page_size: 10000, ...filter })).results;

const getStudent = async (id) =>
    (await api.get(`api/accounts/students/${id}`)).data;

const getParentsPaginated = async (filter) =>
    (await api.get("api/accounts/parents/all", { params: filter })).data;

const getParents = async (filter) =>
    (await getParentsPaginated({ page_size: 10000, ...filter })).results;

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
	getTeachersPaginated,
    getTeacher,
    getStudents,
	getStudentsPaginated,
    getStudent,
    getParents,
	getParentsPaginated,
    getParent,
    getUser,
    getTeacherInfoFromObj,
    getStudentInfoFromObj,
    updateStudent,
    updateUser,
    getStudentStats,
};
