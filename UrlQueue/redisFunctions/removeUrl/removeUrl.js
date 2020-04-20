import asyncRedis from '../asyncRedis.js';
import databaseObjects from '../../configuration/databaseObjects.js'

export default async function removeUrl(keys){
    const client = await databaseObjects.getClient();
    const asyncDelete = await asyncRedis.delete(client);

    keys = JSON.parse(keys);
    let res = await asyncDelete(keys);

    return JSON.stringify(res);
}