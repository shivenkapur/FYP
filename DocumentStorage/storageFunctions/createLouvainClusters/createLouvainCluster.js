export default function createLouvainCluster(){

    return {
        "statement" : `CALL gds.louvain.write({
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
        YIELD communityCount, modularity, modularities`,
        "parameters": { }
      };

}


