import api from "@/services/api";

const images = [
    require("@/assets/classrooms/classroom1.png"),
    require("@/assets/classrooms/classroom2.png"),
    require("@/assets/classrooms/classroom3.png"),
]; 

const getClassroom = async (id) =>
    (await api.get(`api/allocation/classrooms/${id}`)).data;

const getClassrooms = async (filter) =>
    (await api.get(`api/allocation/classrooms/all`, { params: filter })).data;

const updateClassroom = async (classroom) =>
    await api.put(`api/allocation/classrooms/${classroom.id}/`, classroom);

const addTeacherToClassroom = async (classroom, teacherId) => {
    classroom.other_teachers.push(teacherId);
    await updateClassroom(classroom);
};

const getClassroomImage = () => {
    const index = Math.floor(Math.random() * images.length);
    return images[index];
};

const removeTeacherFromClassroom = async (classroom, teacherId) => {
    classroom.other_teachers.splice(
        classroom.other_teachers.indexOf(teacherId),
        1,
    );
    await updateClassroom(classroom);
};

const addStudentToClassroom = async (classroom, studentId) => {
    classroom.students.push(studentId);
    await updateClassroom(classroom);
};

const removeStudentFromClassroom = async (classroom, studentId) => {
    classroom.students.splice(classroom.students.indexOf(studentId), 1);
    await updateClassroom(classroom);
};

const getClassroomInfoFromObj = (item) => ({
    title: item.name,
    subtitle: `Grade ${item.standard}`,
    value: item.id,
});

export {
    getClassroom,
    getClassrooms,
    updateClassroom,
    getClassroomImage,
    addTeacherToClassroom,
    removeTeacherFromClassroom,
    addStudentToClassroom,
    removeStudentFromClassroom,
    getClassroomInfoFromObj,
};
