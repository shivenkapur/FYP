import { strict } from "assert";

export default function getCommunityUrls(communities){

    return {
        "statement" : `MATCH (doc:Document) WHERE doc.community in $communities RETURN doc`,
        "parameters": { communities: communities }
      };
      
}


