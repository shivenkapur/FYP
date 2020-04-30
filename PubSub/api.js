import publish from './pubSubFunctions/publish/publish.js';
import subscribe from './pubSubFunctions/subscribe/subscribe.js';

export default {
    publish: async function (channel, message){
        const response = await publish(channel, message);
        return response;
    },
    subscribe: async function (channel, callback){
        const response = await subscribe(channel, callback);
        return response;
    }
}