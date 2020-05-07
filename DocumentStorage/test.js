import stackTransactions from './storageFunctions/stackTransactions.js';
import sendTransactions from './storageFunctions/sendTransactions.js';

import createLouvainClusters from './storageFunctions/createLouvainClusters/createLouvainCluster.js';
import getCommunities from './storageFunctions/getCommunities/getCommunities.js';
import getCommunityUrls from './storageFunctions/getCommunityUrls/getCommunityUrls.js';
import pubsub from 'pubsub';

async function start(){

    let result = results[1].data;
    
    let communities = [];
    let rowDict = result[0];
    communities.push(rowDict.row[0]);

    //for(let resultIndex in result){
    //  let rowDict = result[resultIndex];
    //  communities.push(rowDict.row[0]);
    //}
    
    sendTransactions(stackTransactions([getCommunityUrls(communities)]) ,function(err, res){
      console.log(res.body.results[0].data);
    })
  }); 

}

start()

