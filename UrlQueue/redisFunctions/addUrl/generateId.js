let crypto = require('crypto');

export default async function generateId(){

    let bufferToken = await crypto.randomBytes(32);
    let stringToken = await bufferToken.toString('base64');

    return stringToken;
}
