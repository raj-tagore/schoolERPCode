import api from "@/services/api";

const getSubjects = async (filter) => 
    (
        await api.get(
            `api/allocation/subjects/all/${filter ? "?" : ""}${filter ? new URLSearchParams(filter) : ""}`,
        )
    ).data;

const getSubject = async (id) =>
    (await api.get(`api/allocation/subjects/${id}`)).data;

const getSubjectInfoFromObj = (item) => ({
    title: item.name,
    subtitle: item.classroom_details ? item.classroom_details.name : 'classroom loading...',
    value: item.id,
});

export { getSubjects, getSubject, getSubjectInfoFromObj };
