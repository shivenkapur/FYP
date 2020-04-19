export default function(keywords, page){
    let urlString = 'https://www.google.com/search?q=';
    let keywordString = '';
    let pageString = `&start=${page*10}`;

    for(let keywordIndex in keywords){
        let keyword = keywords[keywordIndex];
        keywordString += `${keyword}+`
    }

    return `${urlString}${keywordString}${pageString}`
}