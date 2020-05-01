import createNode from './storageFunctions/createNode/createNode.js';
import createRelationship from './storageFunctions/createRelationship/createRelationship.js';
import getNodes from './storageFunctions/getNodes/getNodes.js';
import pubsub from 'pubsub';
import { link } from 'fs';
export default {
    createNode: async function (id, text){
        let jsonReturn = await createNode(id, text);

        const stringJson = JSON.stringify(jsonReturn);
    },
    createRelationship: async function (idLinkFrom, idLinkTo , matchingKeywords = []){
        let jsonReturn = createRelationship(idLinkFrom, idLinkTo, matchingKeywords);

        const stringJson = JSON.stringify(jsonReturn);
    },
    getNodes: async function (){
        let jsonReturn = await getNodes();

        const stringJson = JSON.stringify(jsonReturn);
    },
    getUrlLinkage: async function(){
        pubsub.subscribe('documentData', (channel, message) => {

            message = JSON.parse(message);
            console.log(typeof(message));
            this.createNode(message['url'], message['pageText']);
            
            let linkedTo = message['linkedTo'];

            for(let linkIndex in linkedTo){
                let link = linkedTo[linkIndex];
                this.createNode(link, "");
                this.createRelationship(message['url'], link);
            }
            
        });
        
    }
}