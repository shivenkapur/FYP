const neo4j = require('neo4j-driver');
const driver = neo4j.driver('neo4j://localhost:7687', neo4j.auth.basic('neo4j', 'FYP2020'))
const session = driver.session()

import createNode from './storageFunctions/createNode/createNode.js';
import setupDatabase from './storageFunctions/setupDatabase.js';
import createRelationship from './storageFunctions/createRelationship/createRelationship.js';
import getNodes from './storageFunctions/getNodes/getNodes.js';

async function start(){
  await setupDatabase();
  await getNodes();
}

start()


//CREATE (doc:Document { id: "2", text: "ajjasldjaskjdaskdjkadjla;dakl"})
//MATCH (doc:Document) WHERE doc.id = "1" RETURN doc;
//(rvb)-[:KNOWS]->(ally)
//(doc1)-[:LINKSTO {matchingKeywords: ['hi','bye','sigh']]->(doc2),


/*
GET ALL
MATCH (doc:Document) WHERE true RETURN doc;
*/


/*
CREATE A RELATIONSHIP
MATCH (doc1:Document) WHERE doc1.id = "1" 
MATCH (doc2:Document) WHERE doc2.id = "2"
CREATE (doc1)-[r:LINKSTO { matchingKeywords: ['Zachry']}]->(doc2)
RETURN doc1, doc2, r;*/