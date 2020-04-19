const redis = require("redis");
import databaseObjects from '../configuration/databaseObjects.js'
export default async function setupDatabase(){
    const client = redis.createClient();

    client.on('connect', function() {
        console.log('Redis client connected');
    });
    client.on('error', function (err) {
        console.log('Something went wrong ' + err);
    });

    databaseObjects.setClient(client);
}



