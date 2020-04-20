import asyncRedis from '../asyncRedis.js';
import databaseObjects from '../../configuration/databaseObjects.js'

export default async function getUrl(key){
    
    const client = await databaseObjects.getClient();
    const asyncGet = await asyncRedis.get(client);
    const urlObject = await asyncGet(key);

    return urlObject;
}