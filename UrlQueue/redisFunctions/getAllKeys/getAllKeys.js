import asyncRedis from '../../asyncRedis.js';
import databaseObjects from '../../configuration/databaseObjects.js'

export default async function getUrl(key){
    
    const client = databaseObjects.getClient();
    
    const asyncKeys = await asyncRedis.keys(client);
    
    const urlObject = asyncKeys('*');

    return urlObject;
}