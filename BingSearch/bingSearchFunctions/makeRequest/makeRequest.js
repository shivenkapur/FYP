const fetch = require("node-fetch");
const HttpsProxyAgent = require('https-proxy-agent');

export default async function makeRequest(bingUrl){
    const response = await fetch(bingUrl);// { agent:new HttpsProxyAgent('167.99.184.76:5836')});
    let html = await response.text();
    
    let fs = require('fs');
    fs.writeFileSync('out.html', html)
    return html
    
}


