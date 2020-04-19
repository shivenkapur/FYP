import createUrl from './createUrl/createUrl.js';
import makeRequest from './makeRequest/makeRequest.js';
import getSearchData from './getSearchData/getSearchData.js'

async function start(){

    const searchKeywords = 'node.js best practices';
    const startIndex = 0;//increments of 10

    let googleUrl = await createUrl(searchKeywords, startIndex);

    let html = await makeRequest(googleUrl);

    let searchData = await getSearchData(html);
    console.log(searchData);
}

start();