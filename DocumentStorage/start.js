import api from './api.js';
import pubsub from 'pubsub';

function start(){
    api.getUrlLinkage();
    api.getUrlKeywords();

    api.startClustering();
}   

start();

//MATCH (n) DETACH DELETE n;