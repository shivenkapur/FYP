import getSearchUrl from './utils/getSearchUrl.js'
const axios = require('axios');
const cheerio = require('cheerio');

let searchUrl = getSearchUrl('student'.split(' '), 0);
//searchUrl = 'https://www.hku.hk/';

const $ = cheerio.load('<h2 class="title">Hello world</h2>')

console.log($('.title').text());


fetchData(searchUrl).then( (res) => {
    const html = res.data;

    /*let fs = require('fs');
    fs.writeFile('helloworld.html', html, function (err) {
        if (err) return console.log(err);
    });*/
    const $ = cheerio.load(html);

    const statsTable = $('div.g');
    console.log(statsTable.length);
    statsTable.each(() => {
        console.log($(this).html());
        let title = $(this).find('div.kCrYT > a > div:nth-child(1)').text();
        let link = $(this).find('div.kCrYT > a > div:nth-child(2)').text();
        let metaText1 = $(this).find('div:nth-child(3) > div > div > div > div > div.BNeawe').text();
        let metaText2 = $(this).find('div:nth-child(1) > a > div:nth-child(1)').text();

        console.log(title, link, metaText1, metaText2);
    });
});

async function fetchData(url){
    console.log("Crawling data...")
    // make http call to url
    let response = await axios(url).catch((err) => console.log(err));
    
    if(response.status !== 200){
        console.log("Error occurred while fetching data");
        return;
    }
    return response;
}

//'#main > div > div > div:nth-child(1) > a > div:nth-child(1)'
//'#main > div > div > div:nth-child(1) > a > div:nth-child(2)'
//'#main > div > div > div:nth-child(3) > div > div > div > div > div.BNeawe'
//document.querySelectorAll('#main > div > div > div:nth-child(3) > div > div > div > div > div >div.BNeawe')[0].textContent

