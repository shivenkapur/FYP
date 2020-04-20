import addUrl from './redisFunctions/addUrl/addUrl.js';
import removeUrl from './redisFunctions/removeUrl/removeUrl.js';
import getAllKeys from './redisFunctions/getAllKeys/getAllKeys.js';
import getAllUrls from './redisFunctions/getAllUrls/getAllUrls.js';

export default {
    addUrl: async function (req, res){
        const { url, keywords } = req.body;
        const jsonReturn = await addUrl(url, keywords);
        const stringJson = JSON.stringify(jsonReturn);

        res.send(stringJson);
    },
    removeUrl: async function (req, res){
        const { key } = req.body;
        const jsonReturn = await removeUrl(key);

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson);
    },
    getAllKeys: async function (req, res){
        const jsonReturn = await getAllKeys();

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson);
    },
    getAllUrls: async function (req, res){
        const jsonReturn = await getAllUrls();

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson);
    }
}