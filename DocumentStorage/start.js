import api from './api.js';

function start(){
    api.getUrlLinkage();
}   

start();

//MATCH (n) DETACH DELETE n;