

//get number of websites linking to a particular keyword
MATCH (a)-[:ContainsKeyword]->(b)
RETURN b, COLLECT(b) as keywords
ORDER BY SIZE(keywords) DESC LIMIT 10


//get keywords with max website links
MATCH (keyword:Keyword)
RETURN keyword, size(()-->(keyword)) AS count
ORDER BY count DESC

//get closenes between two keywords
MATCH (key1:Keyword {id: 'Award'})
MATCH (key2:Keyword {id: 'HKU'})
RETURN gds.alpha.linkprediction.commonNeighbors(key1, key2, {relationshipQuery: "ContainsKeyword"}) AS score


//LOUVAIN
CALL gds.louvain.write({
    nodeProjection: 'Document',
    relationshipProjection: {
        TYPE: {
            type: 'LINKSTO',
            orientation: 'undirected',
            aggregation: 'NONE'
        }
    },
    writeProperty: 'community'
})
YIELD communityCount, modularity, modularities




