import setupDatabase from '../storageFunctions/setupDatabase.js';

let client = undefined;
export default {
    setClient: function setClient(clientObject){
        client = clientObject;
    },
    getClient: async function getClient(){
        if(client == undefined){
            await setupDatabase();
        }
        return client;
    }
}