import publish from './redisFunctions/publish/publish.js';
import subscribe from './redisFunctions/subscribe/subscribe.js';

export default {
    publish: async function (channel, message){
        const response = await publish(channel, message);
        return response;
    },
    subscribe: async function (){
        const response = await subscribe(channel, callback);
        return response;
    }
}