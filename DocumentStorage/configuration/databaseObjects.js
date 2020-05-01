import setupDatabase from '../storageFunctions/setupDatabase.js';

let client = undefined;
export default {
    setClient: function setClient(clientObject){
        client = clientObject;
    },
    getClient: async function getClient(){
        
        if(client == undefined || client._open == false){
            await setupDatabase();
            console.log(client._open)
        }
        return client;
    }
}