const getRecords = async (filter) =>
    (
        await api.get("api/finances/records/all", {
            params: filter,
        })
    ).data;

const getRecordInfoFromObj = (item) => ({
    title: item.amount,
    subtitle: item.student_details.user_details.full_name,
    value: item.id,
});

const getPaymentPurposes = async (filter) =>
    (
        await api.get("api/finances/purpose/all", {
            params: filter,
        })
    ).data;

const getPaymentPurposeInfoFromObj = (item) => ({
    title: item.name,
    subtitle: item.description,
    value: item.id,
});

const getPayees = async (filter) =>
    (
        await api.get("api/finances/payees/all", {
            params: filter,
        })
    ).data;

const getPayeeInfoFromObj = (item) => ({
    title: item.email,
    subtitle: item.phone,
    value: item.id,
});

export {
    getRecords,
    getPaymentPurposes,
    getPaymentPurposeInfoFromObj,
    getRecordInfoFromObj,
    getPayees,
    getPayeeInfoFromObj,
};
