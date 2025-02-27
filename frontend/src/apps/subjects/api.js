import { api } from "@/services/api";

const getSubjects = async (filter) =>
    (await api.get("api/allocation/subjects/all", { params: { page_size: 10000, ...filter } })).data;

const getSubject = async (id) =>
    (await api.get(`api/allocation/subjects/${id}`)).data;

const getSubjectInfoFromObj = (item) => ({
    title: item.name,
    subtitle: item.classroom_details
        ? item.classroom_details.name
        : "classroom loading...",
    value: item.id,
});

const updateSubject = async (subject) => {
    const { classroom, teacher, ...cleanSubject } = JSON.parse(
        JSON.stringify(subject),
    );
    await api.put(`api/allocation/subjects/${subject.id}/`, cleanSubject);
};

const createSubject = async (subject) =>
    await api.post("api/allocation/subjects/create/", subject);

export {
    getSubjects,
    getSubject,
    getSubjectInfoFromObj,
    updateSubject,
	createSubject,
};
