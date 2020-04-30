var redis = require("redis")
  , subscriber = redis.createClient();
  
export default async function subscribe(channel, callback){

    subscriber.on("message", callback);
    subscriber.subscribe(channel);
}
