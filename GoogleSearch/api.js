import getSearchData from "./apiFunctions/getSearchData/getSearchData.js";

export default {
    getAllLinks: async function (req, res){
        const { searchKeywords } = req.query;
        let jsonReturn = await getSearchData(searchKeywords, false);

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson); 
    },
    getAllMetaData: async function (req, res){
        const { searchKeywords } = req.query;
        let jsonReturn = await getSearchData(searchKeywords, true);

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson); 
    }
}