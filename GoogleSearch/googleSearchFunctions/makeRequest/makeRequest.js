const fetch = require("node-fetch");
const HttpsProxyAgent = require('https-proxy-agent');

export default async function makeRequest(googleUrl){
    const response = await fetch(googleUrl);// { agent:new HttpsProxyAgent('167.99.184.76:5836')});
    let html = await response.text();

    console.log(html)
    return html
}


