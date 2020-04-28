import publish from './pubSubFunctions/publish/publish.js';
import subscribe from './pubSubFunctions/subscribe/subscribe.js';

async function test(){

    let response = await subscribe();
    console.log(response);

    response = await publish("temp-reading:living-room", "Yeh hain sadda message!");
    console.log(response);   

}

test();