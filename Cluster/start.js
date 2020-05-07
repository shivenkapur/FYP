import api from './api.js';

function start(){
    api.getClusters();
}   

start();

//MATCH (n) DETACH DELETE n;