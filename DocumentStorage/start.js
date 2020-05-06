import api from './api.js';

function start(){
    api.getUrlLinkage();
    api.getUrlKeywords();
}   

start();

//MATCH (n) DETACH DELETE n;