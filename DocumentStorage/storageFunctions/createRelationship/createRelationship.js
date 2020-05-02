export default function createRelationship(idLinkFrom, idLinkTo, matchingKeywords = []){

    return {
        'statement' : `
            MATCH (doc1:Document) WHERE doc1.id = $idLinkFrom
            MATCH (doc2:Document) WHERE doc2.id = $idLinkTo
            MERGE (doc1)-[r:LINKSTO { matchingKeywords: $matchingKeywords }]->(doc2)
            RETURN doc1, doc2, r;
        `,
        "parameters": { "idLinkFrom": `${idLinkFrom}` , "idLinkTo": `${idLinkTo}`, "matchingKeywords" : `${matchingKeywords}`}
    };
}

