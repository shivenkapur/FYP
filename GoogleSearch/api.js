import getSearchData from "./apiFunctions/getSearchData/getSearchData.js";

export default {
    getAllLinks: async function (searchKeywords){
        return await getSearchData(searchKeywords, false);
    },
    getAllMetaData: async function (searchKeywords){
        return await getSearchData(searchKeywords, true);
    }
}