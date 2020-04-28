var redis = require("redis")
  , subscriber = redis.createClient()
  , client = redis.createClient();
  
export default async function publish(){

    subscriber.on("message", function(channel, message) {
        console.log("Message: " + message + " Channel:" + channel);
      });
      
    subscriber.subscribe("temp-reading:living-room");
}
