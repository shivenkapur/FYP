import setupDatabase from './redisFunctions/setupDatabase.js';
import addUrl from './redisFunctions/addUrl/addUrl.js';
import getUrl from './redisFunctions/getUrl/getUrl.js';
import removeUrls from './redisFunctions/removeUrls/removeUrls.js';
import getAllKeys from './redisFunctions/getAllKeys/getAllKeys.js';

async function test(){
    await setupDatabase();
    //await addUrl('www.google.com');

    let keys = await getAllKeys();
    console.log(keys , 'Hiii');

    let deleteKeys = ['mqWwD3GfwnKBUeKI1poF7xHvvv0FYgSln2gXdv3x7EM=', 'CPhKppbVwZoKODa/LYoHzGh2P6KQnSE8lifecx6Qc3s=', 'hpv6koo5Xwn2UCRDOYIujk0IQEsdvC5L6PkiRcEPupw='];
    removeUrls(deleteKeys);

    keys = await getAllKeys();
    console.log(keys , 'Hiii');
    
}

test();