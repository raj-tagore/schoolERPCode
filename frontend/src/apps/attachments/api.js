// Form needs to be FormData
const uploadAttachment = async (form) =>
    (await api.post("api/attachments/create", form)).data;

const getAttachments = async (filters) =>
    (await api.post("api/attachments/all", filters)).data;


export {
	uploadAttachment,
	getAttachments,
};
