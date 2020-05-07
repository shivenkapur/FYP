var redis = require("redis");
  
export default async function subscribe(channel, callback){

  let subscriber = redis.createClient();
  subscriber.on("message", callback);
  subscriber.subscribe(channel);
}
