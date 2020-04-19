let util = require('util');
var querystring = require('querystring');
let URL = '%s://www.google.com/search?hl=%s&q=%s&start=%s&sa=N&num=%s&ie=UTF-8&oe=UTF-8&gws_rd=ssl';

let lang = 'en'
let protocol = 'https'
// start parameter is optional
export default async function google (query, start, resultsPerPage = 10) {
    let googleUrl = util.format(URL, protocol, lang, querystring.escape(query), start, resultsPerPage)
    return googleUrl;
}



  