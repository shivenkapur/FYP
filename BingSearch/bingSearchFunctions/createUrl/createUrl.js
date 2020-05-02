let util = require('util');
var querystring = require('querystring');
let URL = '%s://www.bing.com/search?q=%s&first=%s&count=%s';
let protocol = 'https'
// start parameter is optional
export default async function bing (query, start, resultsPerPage = 30) {
    let bingUrl = util.format(URL, protocol, querystring.escape(query), start, resultsPerPage)
    return bingUrl;
}



  