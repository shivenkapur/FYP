let client = undefined;
export default {
    setClient: function setClient(clientObject){
        client = clientObject;
    },
    getClient: function getClient(){
        return client;
    }
}