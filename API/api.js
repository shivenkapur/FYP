import getUrls from './apiFunctions/getUrls/getUrls.js';

export default {
    getUrls: async function (req, res){
        const jsonReturn = await addUrl();
        const stringJson = JSON.stringify(jsonReturn);

        res.send(stringJson);
    },
}