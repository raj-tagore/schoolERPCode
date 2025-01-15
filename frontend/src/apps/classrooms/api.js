import api from "@/services/api";

// Any requests that need to be called multiple times can be defined here

const images = [
    require("@/assets/classrooms/classroom1.png"),
    require("@/assets/classrooms/classroom2.png"),
    require("@/assets/classrooms/classroom3.png"),
];

const getClassroom = async (classroomId) =>
    (await api.get(`api/allocation/classrooms/${classroomId}`)).data;

const getClassrooms = async () =>
    (await api.get("api/allocation/classrooms/all")).data;


const updateClassroom = async (classroom) => {
    await api.put(`api/allocation/classrooms/${classroom.id}/`, classroom);
};

const addTeacherToClassroom = async (classroom, teacherId) => {
    classroom.other_teachers.push(teacherId);
    updateClassroom();
};

const getClassroomImage = async () => {
    const index = Math.floor(Math.random() * images.length);
    return images[index];
};

const removeTeacherFromClassroom = async (classroom, teacherId) => {
    classroom.other_teachers.splice(
        classroom.other_teachers.indexOf(teacherId),
        1,
    );
    updateClassroom();
};

const addStudentToClassroom = async (classroom, studentId) => {
    classroom.students.push(studentId);
    updateClassroom();
};

const removeStudentFromClassroom = async (classroom, studentId) => {
	classroom.students.splice(classroom.students.indexOf(studentId), 1);
	updateClassroom();
}

export {
    getClassroom,
    getClassrooms,
    updateClassroom,
    getClassroomImage,
    addTeacherToClassroom,
	removeTeacherFromClassroom,
	addStudentToClassroom,
	removeStudentFromClassroom,
};
