import asyncRedis from '../../asyncRedis.js';
import databaseObjects from '../../configuration/databaseObjects.js'

export default async function getUrl(key){
    
    const client = databaseObjects.getClient();
    const asyncGet = await asyncRedis.get(client);
    const urlObject = asyncGet(key);

    return urlObject;
}