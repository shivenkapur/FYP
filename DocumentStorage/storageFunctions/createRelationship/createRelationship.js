import databaseObjects from '../../configuration/databaseObjects.js'

export default async function createRelationship(idLinkFrom, idLinkTo, matchingKeywords = []){

    const client = await databaseObjects.getClient();

    try {
        const result = await client.writeTransaction(tx =>
            tx.run(
                `
                    MATCH (doc1:Document) WHERE doc1.id = '${idLinkFrom}'
                    MATCH (doc2:Document) WHERE doc2.id = '${idLinkTo}'
                    CREATE (doc1)-[r:LINKSTO { matchingKeywords: '${matchingKeywords}'}]->(doc2)
                    RETURN doc1, doc2, r;
                `
            )
        );

        return result;
      } catch (error){
          console.log(error);
      }
}