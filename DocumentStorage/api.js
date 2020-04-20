import createNode from './storageFunctions/createNode/createNode.js';
import setupDatabase from './storageFunctions/setupDatabase.js';
import createRelationship from './storageFunctions/createRelationship/createRelationship.js';
import getNodes from './storageFunctions/getNodes/getNodes.js';
import databaseObjects from './configuration/databaseObjects.js'

export default {
    createNode: async function (id, text){
        if(databaseObjects.getClient() == undefined){
            await setupDatabase();
        }
        return await createNode(id, text);
    },
    createRelationship: async function (idLinkFrom, idLinkTo, matchingKeywords){
        if(databaseObjects.getClient() == undefined){
            await setupDatabase();
        }
        return await createRelationship(idLinkFrom, idLinkTo, matchingKeywords);
    },
    getNodes: async function (){
        if(databaseObjects.getClient() == undefined){
            await setupDatabase();
        }
        return await getNodes();
    }
}