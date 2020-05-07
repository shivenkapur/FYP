export default async function getNodes(){

    const client = await databaseObjects.getClient();
    try {
        const result = await client.readTransaction(tx =>
            tx.run(
                `
                    MATCH (doc:Document) WHERE true RETURN doc;
                `
            )
        );

        return result.records;
      } catch (error) {
          console.log(error);
      }
}
