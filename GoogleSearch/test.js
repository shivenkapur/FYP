import api from './api.js'
import pubsub from 'pubsub';

export default async function start(searchKeywords){

    pubsub.subscribe("urlQueue", function(channel, message){
        console.log(channel, message);
    });
    
    let data = await api.getAllLinks('Node.js');

    console.log(data)
    
}

start();