const { promisify } = require('util');

export default {
    keys: async function(client){
        const getKeysAsync = promisify(client.scan).bind(client);
        return getKeysAsync;
    },

    get: async function(client){
        const getAsync = promisify(client.get).bind(client);
        return getAsync;
    },

    delete: async function(client){
        const deleteAsync = promisify(client.unlink).bind(client);
        return deleteAsync;
    }
}