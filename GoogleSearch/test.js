import api from './api.js'


export default async function start(searchKeywords){

    let data = await api.getAllLinks('Why is coronavirus so stupid?');
    console.log(data);

    data = await api.getAllMetaData('Help me corona');
    console.log(data);
    
}

start();