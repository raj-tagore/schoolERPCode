import { api } from "@/services/api";

const getTeachersListing = async (filter) =>
    (await api.get("api/accounts/teachers/all", { params: filter })).data;

const getTeachers = async (filter) =>
    (await getTeachersListing({ page_size: 10000, ...filter })).results;

const getTeacher = async (id) =>
    (await api.get(`api/accounts/teachers/${id}`)).data;

const getStudentsListing = async (filter) =>
    (await api.get("api/accounts/students/all", { params: filter })).data;

const getStudents = async (filter) =>
    (await getStudentsListing({ page_size: 10000, ...filter })).results;

const getStudent = async (id) =>
    (await api.get(`api/accounts/students/${id}`)).data;

const getParentsListing = async (filter) =>
    (await api.get("api/accounts/parents/all", { params: filter })).data;

const getParents = async (filter) =>
    (await getParentsListing({ page_size: 10000, ...filter })).results;

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
	getTeachersListing,
    getTeacher,
    getStudents,
	getStudentsListing,
    getStudent,
    getParents,
	getParentsListing,
    getParent,
    getUser,
    getTeacherInfoFromObj,
    getStudentInfoFromObj,
    updateStudent,
    updateUser,
    getStudentStats,
};
