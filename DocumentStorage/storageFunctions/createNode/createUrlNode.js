export default function createUrlNode(id, text){

    return {
        "statement" : `OPTIONAL MATCH (doc: Document) WHERE doc.id = $id
            FOREACH (_ IN CASE WHEN doc IS NULL THEN [true] ELSE [] END |
            CREATE (docnew:Document) 
            SET docnew.id = $id)`,
        "parameters": { "id": `${id}` }
      };

}

