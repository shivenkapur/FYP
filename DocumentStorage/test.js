import stackTransactions from './storageFunctions/stackTransactions.js';
import sendTransactions from './storageFunctions/sendTransactions.js';

import createLouvainClusters from './storageFunctions/createLouvainClusters/createLouvainCluster.js';
import getCommunities from './storageFunctions/getCommunities/getCommunities.js';
import getCommunityUrls from './storageFunctions/getCommunityUrls/getCommunityUrls.js';
import pubsub from 'pubsub';

async function start(){

  
  pubsub.publish("a", "jklj");

}

start()

