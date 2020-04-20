import createNode from './storageFunctions/createNode/createNode.js';
import createRelationship from './storageFunctions/createRelationship/createRelationship.js';
import getNodes from './storageFunctions/getNodes/getNodes.js';

export default {
    createNode: async function (req, res){
        console.log(req.body);
        const { id, text } = req.body;
        let jsonReturn = await createNode(id, text);

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson);
    },
    createRelationship: async function (req, res){

        console.log(req.body);
        const { idLinkFrom, idLinkTo , matchingKeywords} = req.body;
        let jsonReturn = createRelationship(idLinkFrom, idLinkTo, matchingKeywords);

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson);
    },
    getNodes: async function (req, res){
        let jsonReturn = await getNodes();

        const stringJson = JSON.stringify(jsonReturn);
        res.send(stringJson);
    }
}