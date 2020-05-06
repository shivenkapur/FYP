export default function createKeywordNode(keyword){

    return {
        "statement" : `OPTIONAL MATCH (keyword: Keyword) WHERE keyword.id = $id
            FOREACH (_ IN CASE WHEN keyword IS NULL THEN [true] ELSE [] END |
            CREATE (keywordnew:Keyword) 
            SET keywordnew.id = $id)`,
        "parameters": { "id": `${keyword}` }
      };

}

