import api from './api.js'
import pubsub from 'pubsub';

export default async function start(searchKeywords){

    pubsub.subscribe("urlQueue", function(channel, message){
        console.log(channel, message);
    });
    
    let data = await api.getAllLinks('Why is coronavirus so stupid?');
    console.log(data);

    data = await api.getAllMetaData('Help me corona');
    console.log(data);
    
}

start();