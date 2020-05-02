import createUrl from '../../bingSearchFunctions/createUrl/createUrl.js';
import makeRequest from '../../bingSearchFunctions/makeRequest/makeRequest.js';
import getBingData from '../../bingSearchFunctions/getBingData/getBingData.js';

export default async function getSearchData(searchKeywords, getAllData){

    const startIndex = 0; //increments of 10
    const resultsPerRequest = 100;

    let googleUrl = await createUrl(searchKeywords, startIndex, resultsPerRequest);

    let html = await makeRequest(googleUrl);

    let searchData = await getBingData(html, getAllData);


    return searchData;
}
