const redis = require("redis");
import databaseObjects from '../configuration/databaseObjects.js';
import asyncRedis from './asyncRedis.js';

export default async function setupDatabase(){
    const client = await redis.createClient();

    const asyncOn = await asyncRedis.on(client);

    let connectStatus = await asyncOn('connect');
    console.log("Connected: ", connectStatus);


    /*connectStatus = await asyncOn('error');
    console.log("Error: ", connectStatus);*/
    databaseObjects.setClient(client);
}



