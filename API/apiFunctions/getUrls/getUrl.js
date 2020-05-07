
export default function getCommunities(){

    return {
        "statement" : `MATCH (doc:Document) RETURN DISTINCT doc.community`,
        "parameters": { }
      };
      
}