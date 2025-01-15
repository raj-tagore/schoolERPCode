import api from "@/services/api";

const getTeachers = async (filter) =>
    (
        await api.get(
            `api/accounts/teachers/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getClassroomTeachers = async (classroom) =>
    await Promise.all(
        classroom.other_teachers.map(async (teacher_id) => {
            return (await api.get(`api/accounts/teachers/${teacher_id}/`)).data;
        }),
    );

const getStudents = async (filter) => {
    return (
        await api.get(
            `api/accounts/teachers/all${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;
};

const getClassroomStudents = async (classroom) => {
    await Promise.all(
        classroom.students.map(async (student_id) => {
            return (await api.get(`api/accounts/students/${student_id}/`)).data;
        }),
    );
};

export { getTeachers, getClassroomTeachers, getStudents, getClassroomStudents };
