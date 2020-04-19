import api from './api.js'


export default async function start(searchKeywords){

    let data = await api.getAllLinks('node.js best practices');
    console.log(data);

    data = await api.getAllMetaData('node.js worst practices');
    console.log(data);
    
}

start();