import databaseObjects from '../configuration/databaseObjects.js'

export default async function setupDatabase(){
    
    const neo4j = require('neo4j-driver');
    const driver = neo4j.driver('neo4j://localhost:7687', neo4j.auth.basic('neo4j', 'FYP2020'));
    const session = driver.session();
    databaseObjects.setClient(session);
}



