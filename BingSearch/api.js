import getSearchData from "./apiFunctions/getSearchData/getSearchData.js";
import pubsub from 'pubsub';

export default {
    getAllLinks: async function (searchKeywords){
        let jsonReturn = await getSearchData(searchKeywords, false);
        const stringJson = JSON.stringify(jsonReturn);
        pubsub.publish("urlQueue", stringJson);
        
    },
    getAllMetaData: async function (searchKeywords){
        let jsonReturn = await getSearchData(searchKeywords, true);

        const stringJson = JSON.stringify(jsonReturn);
        pubsub.publish("urlQueue", stringJson);
    }
}
