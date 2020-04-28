const { promisify } = require('util');

export default {
    publish: async function(client){
        const getKeysAsync = promisify(client.publish).bind(client);
        return getKeysAsync;
    },
    on: async function(client){
        const onAsync = promisify(client.on).bind(client);
        return onAsync;
    },
}