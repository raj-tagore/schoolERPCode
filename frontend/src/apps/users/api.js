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


export { getTeachers, getStudents };
