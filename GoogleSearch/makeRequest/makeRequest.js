const fetch = require("node-fetch");

export default async function makeRequest(googleUrl){
    const response = await fetch(googleUrl);
    let html = await response.text();

    return html
}


