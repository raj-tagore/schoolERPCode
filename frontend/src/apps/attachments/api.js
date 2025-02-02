import { api } from "@/services/api";

const createAttachment = async (formObj) => {
    const data = new FormData();
    for (const [key, value] of Object.entries(formObj)) {
        data.append(key, value);
    }
    console.log(data);
    return (
        await api.post("api/attachments/create/", data, {
            headers: { "Content-Type": "multipart/form-data" },
        })
    ).data;
};

const getAttachments = async (filters) =>
    (await api.post("api/attachments/all", filters)).data;

export { createAttachment, getAttachments };
