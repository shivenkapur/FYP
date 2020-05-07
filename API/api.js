import getUrls from './apiFunctions/getUrls/getUrls.js';

export default {
    getUrls: async function (req, res){
        pubsub.subscribe('getNodes', async(channel, message) => {
            
            message = JSON.parse(message)

        });
        // const jsonReturn = await addUrl();
        // const stringJson = JSON.stringify(jsonReturn);

        // res.send(stringJson);
    },

}