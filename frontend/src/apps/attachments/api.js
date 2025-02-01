// Form needs to be FormData
const uploadAttachment = async (form) =>
    (await api.post("api/attachments/create", form)).data;

export {
	uploadAttachment,
};
