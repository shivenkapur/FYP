const cheerio = require('cheerio');

export default async function getSearchData(html, allData){
    
    let $ = cheerio.load(html);

    let searchCards = $('#b_results');
    let searchData = [];

    let children = [Array.from(searchCards.children())[0]];
    children.forEach((element) => {
        let url = $('.b_algo > .b_title > h2 > a', element).attr('href');
        if(url != undefined){
            
            if(!allData){
                searchData.push({ url: '/url?q=' + url });
            } else{
                let title = $('.b_algo > .b_title > h2 > a', element).text();
                let metaDescription = $('.b_algo > .b_caption > p', element).text();
                
                searchData.push({
                    url: '/url?q=' + url,
                    title: title,
                    metaDescription: metaDescription
                });
            }
            
        } 
    });

    return searchData;
}