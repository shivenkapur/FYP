export default function createKeywordRelationship(url, keyword){

    return {
        'statement' : `
            MATCH (doc:Document) WHERE doc.id = $url
            MATCH (keyword:Keyword) WHERE keyword.id = $keyword
            MERGE (doc)-[r:ContainsKeyword]-(keyword)
            RETURN doc, keyword, r;
        `,
        "parameters": { "url": `${url}` , "keyword": `${keyword}`}
    };
}

