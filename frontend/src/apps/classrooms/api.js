import api from "@/services/api";

// Any requests that need to be called multiple times can be defined here

const getClassroom = async (classroomId) =>
    (await api.get(`api/allocation/classrooms/${classroomId}`)).data;

const getClassrooms = async () =>
    (await api.get("api/allocation/classrooms/all")).data;

const getClassroomSubjects = async (classroomId) =>
    (await api.get(`api/allocation/subjects/all/?classroom=${classroomId}`)).data;

export { getClassroom, getClassrooms, getClassroomSubjects };