import getAllKeys from '../getAllKeys/getAllKeys.js';
import getUrl from '../getUrl/getUrl.js';

export default async function getAllUrls(){

    let keys = await getAllKeys();

    keys = JSON.parse(keys)[1];

    let values = [];
    for(let keyIndex in keys){
        let key = keys[keyIndex];
        const url = await getUrl(key);
        values.push(url);
    }

    const stringJson = JSON.stringify(values);
    return stringJson;
}