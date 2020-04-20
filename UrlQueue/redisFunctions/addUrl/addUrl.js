import generateId from './generateId.js';
import databaseObjects from '../../configuration/databaseObjects.js';

export default async function addUrl(url, keywords){

    const client = await databaseObjects.getClient();

    const newId = await generateId();
    const urlObject = {
        url: url,
        keywords: keywords
    };

    var stringJson = JSON.stringify(urlObject);
    client.set(newId, stringJson);

    return stringJson;
}
