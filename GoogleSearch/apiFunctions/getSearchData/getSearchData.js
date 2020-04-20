import createUrl from '../../googleSearchFunctions/createUrl/createUrl.js';
import makeRequest from '../../googleSearchFunctions/makeRequest/makeRequest.js';
import getGoogleData from '../../googleSearchFunctions/getGoogleData/getGoogleData.js'


export default async function getSearchData(searchKeywords, getAllData){

    const startIndex = 0; //increments of 10
    const resultsPerRequest = 100;

    let googleUrl = await createUrl(searchKeywords, startIndex, resultsPerRequest);

    let html = await makeRequest(googleUrl);

    let searchData = await getGoogleData(html, getAllData);

    return searchData;
}
