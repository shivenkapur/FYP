import createUrlNode from './storageFunctions/createNode/createUrlNode.js';
import createKeywordNode from './storageFunctions/createNode/createKeywordNode.js';

import createNodeRelationship from './storageFunctions/createRelationship/createNodeRelationship.js';
import createKeywordRelationship from './storageFunctions/createRelationship/createKeywordRelationship.js';

import pubsub from 'pubsub';

import stackTransactions from './storageFunctions/stackTransactions.js';
import sendTransactions from './storageFunctions/sendTransactions.js';

import createLouvainClusters from './storageFunctions/createLouvainClusters/createLouvainCluster.js';
import getCommunities from './storageFunctions/getCommunities/getCommunities.js';
import getCommunityUrls from './storageFunctions/getCommunityUrls/getCommunityUrls.js';

export default {
    getUrlLinkage: async function(){
        
        pubsub.subscribe('documentData', async (channel, message) => {

            console.log(channel)
            message = JSON.parse(message);

            let transactions = [];

            transactions.push(createUrlNode(message['url'], message['pageText']));


            let linkedTo = message['linkedTo'];

            for(let linkIndex in linkedTo){
                let link = linkedTo[linkIndex];
                transactions.push(createUrlNode(link, ""));
                transactions.push(createNodeRelationship(message['url'], link));
            }

            let statements = stackTransactions(transactions);
            console.log(message.url);
            sendTransactions(statements);
        });
        console.log("Subscribed to Document Data");
    },

    getUrlKeywords: async function(){
        
        
        pubsub.subscribe("urlKeywords", async (channel, message) => {
            console.log(channel)
            message = JSON.parse(message);

            let transactions = [];

            let keywords = message['keywords'];

            for(let keywordIndex in keywords){
                let keyword = keywords[keywordIndex];
                transactions.push(createKeywordNode(keyword));
                transactions.push(createKeywordRelationship(message['url'], keyword));
            }

            let statements = stackTransactions(transactions);
            console.log(statements);
            sendTransactions(statements);
        });
        console.log("Subscribed to Url Keywords");
    },

    startClustering: async function(){

        pubsub.subscribe("startClustering", async (channel, message) => {
            let statements = stackTransactions([createLouvainClusters(), getCommunities()]);
            

            sendTransactions(statements, function(err, res) {
                let results = res.body.results;
                console.log(results)
                let result = results[1].data;
                
                let communities = [];

                for(let itemIndex in result){
                    let rowDict = result[itemIndex];
                    communities.push(rowDict.row[0]);
                }

                    
                sendTransactions(stackTransactions([getCommunityUrls(communities)]) ,function(err, res){
                    pubsub.publish("clusterDocuments", JSON.stringify(res.body.results[0].data));
                });
            }); 
        });
    }
}