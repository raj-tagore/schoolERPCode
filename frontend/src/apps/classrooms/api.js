import { api } from "@/services/api";

const images = [
    require("@/assets/classrooms/classroom1.png"),
    require("@/assets/classrooms/classroom2.png"),
    require("@/assets/classrooms/classroom3.png"),
];

const getClassroom = async (id) =>
    (await api.get(`api/allocation/classrooms/${id}`)).data;

const getClassrooms = async (filter) =>
    (await api.get("api/allocation/classrooms/all", { params: { page_size: 10000, ...filter } })).data;

const updateClassroom = async (classroom) =>
    await api.put(`api/allocation/classrooms/${classroom.id}/`, classroom);

const getClassroomImage = () => {
    const index = Math.floor(Math.random() * images.length);
    return images[index];
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
    getClassroomInfoFromObj,
};
