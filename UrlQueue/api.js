import addUrl from './redisFunctions/addUrl/addUrl.js';
import removeUrl from './redisFunctions/removeUrl/removeUrl.js';
import getAllKeys from './redisFunctions/getAllKeys/getAllKeys.js';
import getAllUrls from './redisFunctions/getAllUrls/getAllUrls.js';

export default {
    addUrl: async function (req, res){
        const { url, keywords } = req.body;
        const jsonReturn = await addUrl(url, keywords);
        res.send(jsonReturn);
    },
    removeUrl: async function (req, res){
        const { key } = req.body;
        const jsonReturn = await removeUrl(key);
        res.send(jsonReturn);
    },
    getAllKeys: async function (req, res){
        const jsonReturn = await getAllKeys();
        res.send(jsonReturn);
    },
    getAllUrls: async function (req, res){
        const jsonReturn = await getAllUrls();
        res.send(jsonReturn);
    }
}