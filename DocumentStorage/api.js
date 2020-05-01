import createNode from './storageFunctions/createNode/createNode.js';
import createRelationship from './storageFunctions/createRelationship/createRelationship.js';
import getNodes from './storageFunctions/getNodes/getNodes.js';

export default {
    createNode: async function (id, text){
        let jsonReturn = await createNode(id, text);

        const stringJson = JSON.stringify(jsonReturn);
    },
    createRelationship: async function (idLinkFrom, idLinkTo , matchingKeywords){
        let jsonReturn = createRelationship(idLinkFrom, idLinkTo, matchingKeywords);

        const stringJson = JSON.stringify(jsonReturn);
    },
    getNodes: async function (){
        let jsonReturn = await getNodes();

        const stringJson = JSON.stringify(jsonReturn);
    },
    getUrlLinkage: async function(){
        
    }
}