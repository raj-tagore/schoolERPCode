import api from "@/services/api";

const getTeachers = async (filter) =>
    (
        await api.get(
            `api/accounts/teachers/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getStudents = async (filter) => 
    (
        await api.get(
            `api/accounts/students/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getTeacherInfoFromObj = (item) => ({
    title: `${item.user.full_name}`,
    subtitle: item.identifier,
    value: item.id,
});

export { getTeachers, getStudents, getTeacherInfoFromObj };
