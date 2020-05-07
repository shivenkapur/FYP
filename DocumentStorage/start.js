import api from './api.js';
import pubsub from 'pubsub';

function start(){
    api.getUrlLinkage();
    api.getUrlKeywords();

    api.getCentralKeywords();
    pubsub.publish("startClustering", "jklj");
}   

start();

//MATCH (n) DETACH DELETE n;