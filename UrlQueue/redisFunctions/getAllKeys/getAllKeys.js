import asyncRedis from '../asyncRedis.js';
import databaseObjects from '../../configuration/databaseObjects.js'

export default async function getAllKeys(){
    
    const client = await databaseObjects.getClient();
    
    const asyncKeys = await asyncRedis.keys(client);
    
    const urlObject = await asyncKeys(0);

    const stringJson = JSON.stringify(urlObject);

    return stringJson;
}