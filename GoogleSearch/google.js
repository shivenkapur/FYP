var request = require('request')
var cheerio = require('cheerio')
var querystring = require('querystring')
var util = require('util')

var linkSel = 'h3.r a'
var descSel = 'div.s'
var itemSel = 'div.g'
var nextSel = 'td.b a span'



  var requestOptions = {
    url: newUrl,
    method: 'GET'
  }

  for (var k in google.requestOptions) {
    requestOptions[k] = google.requestOptions[k]
  }

  request(requestOptions, function (err, resp, body) {
    console.log(resp.statusCode);
    if ((err == null) && resp.statusCode === 200) {
      var $ = cheerio.load(body)
      var res = {
        url: newUrl,
        query: query,
        start: start,
        links: [],
        $: $,
        body: body
      }

      $(itemSel).each(function (i, elem) {
        console.log(elem.html())
        var linkElem = $(elem).find(linkSel)
        var descElem = $(elem).find(descSel)
        var item = {
          title: $(linkElem).first().text(),
          link: null,
          description: null,
          href: null
        }
        var qsObj = querystring.parse($(linkElem).attr('href'))

        if (qsObj['/url?q']) {
          item.link = qsObj['/url?q']
          item.href = item.link
        }

        $(descElem).find('div').remove()
        item.description = $(descElem).text()

        res.links.push(item)
      })

      if ($(nextSel).last().text() === google.nextText) {
        res.next = function () {
          igoogle(query, start + google.resultsPerPage, callback)
        }
      }
      console.log(res.links);
      callback(null, res)
    } else {
      callback(new Error('Error on response' + (resp ? ' (' + resp.statusCode + ')' : '') + ':' + err + ' : ' + body), null, null)
    }
  })
}

module.exports = google
