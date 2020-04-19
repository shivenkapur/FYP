let util = require('util');
var querystring = require('querystring');
let URL = '%s://www.google.%s/search?hl=%s&q=%s&start=%s&sa=N&num=%s&ie=UTF-8&oe=UTF-8&gws_rd=ssl';

let resultsPerPage = 10
let tld = 'com'
let lang = 'en'
let requestOptions = {}
let nextText = 'Next'
let protocol = 'https'
// start parameter is optional
export default async function google (query, start) {
    let googleUrl = util.format(URL, protocol, tld, lang, querystring.escape(query), start, resultsPerPage)
    return googleUrl;
}



  