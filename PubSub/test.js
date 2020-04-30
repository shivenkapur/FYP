import api from './api';
async function test(){

    let response = await api.subscribe("urlQueue", function(channel, message){
        console.log(channel, message);
    });
    console.log(response);

    response = await api.publish("urlQueue", "Niente");
    console.log(response);   

}

test();