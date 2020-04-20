import databaseObjects from '../../configuration/databaseObjects.js'

export default async function createNode(id, text){

    const client = await databaseObjects.getClient();
    try {
        const result = await client.writeTransaction(tx =>
            tx.run(
                `
                    CREATE (doc:Document) 
                    SET doc.id = $id , doc.text = $text
                    RETURN doc.id + ", from node " + id(doc)
                `,
                { id: `${id}` , text: `${text}`}
            )
        );
      
        const singleRecord = result.records[0]
        const docId = singleRecord.get(0)
      
        console.log(docId)
      } catch (error){
          console.log(error);
      }
}