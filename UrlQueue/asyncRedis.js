const { promisify } = require('util');

export default {
    keys: async function(client){
        const getKeysAsync = promisify(client.keys).bind(client);
        return getKeysAsync;
    },

    get: async function(client){
        const getAsync = promisify(client.hgetall).bind(client);
        return getAsync;
    }
}