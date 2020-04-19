const cheerio = require('cheerio');

export default async function getSearchData(html, allData){
    let $ = cheerio.load(html);

    let searchCards = $('#main > div > div.ZINbbc.xpd.O9g5cc.uUPGi');

    let searchData = [];
    searchCards.each(function () {
        let url = $(this).find('div.kCrYT > a').attr('href');

        if(url != undefined){
            
            if(!allData){
                searchData.push({ url: url });
            } else{
                let title = $(this).find('div.vvjwJb').text();
                let metaDescription = $(this).find('div.kCrYT > div > div.s3v9rd').text()
                
                searchData.push({
                    url: url,
                    title: title,
                    metaDescription: metaDescription
                });
            }
            
        } 
    });

    return searchData;
}