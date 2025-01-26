import api from "@/services/api";

const getTeachers = async (filter) =>
    (
        await api.get(
            `api/accounts/teachers/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getTeacher = async (id) =>
    (await api.get(`api/accounts/teachers/${id}`)).data;

const getStudents = async (filter) => 
    (
        await api.get(
            `api/accounts/students/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getStudent = async (id) =>
    (await api.get(`api/accounts/students/${id}`)).data;

const getParents = async (filter) => 
    (
        await api.get(
            `api/accounts/parents/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getParent = async (id) =>
    (await api.get(`api/accounts/parents/${id}`)).data;

const getTeacherInfoFromObj = (item) => ({
    title: `${item.user.full_name}`,
    subtitle: item.identifier,
    value: item.id,
});

const getStudentInfoFromObj = (item) => ({
    title: `${item.user.full_name}`,
    subtitle: item.identifier,
    value: item.id,
});

export { 
    getTeachers, 
    getTeacher,
    getStudents, 
    getStudent,
    getParents,
    getParent,
    getTeacherInfoFromObj,
    getStudentInfoFromObj,
};