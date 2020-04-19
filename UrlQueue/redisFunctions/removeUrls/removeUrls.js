import databaseObjects from '../../configuration/databaseObjects.js'

export default async function removeUrls(keys){
    const client = databaseObjects.getClient();
    client.del(keys);
}