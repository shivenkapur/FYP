import createNode from './storageFunctions/createNode/createNode.js';
import createRelationship from './storageFunctions/createRelationship/createRelationship.js';
import getNodes from './storageFunctions/getNodes/getNodes.js';
import pubsub from 'pubsub';

import stackTransactions from './storageFunctions/stackTransactions.js';
import sendTransactions from './storageFunctions/sendTransactions.js'
export default {
    getUrlLinkage: async function(){
        
        pubsub.subscribe('documentData', async (channel, message) => {

            message = JSON.parse(message);

            let transactions = [];

            transactions.push(createNode(message['url'], message['pageText']));


            let linkedTo = message['linkedTo'];

            for(let linkIndex in linkedTo){
                let link = linkedTo[linkIndex];
                transactions.push(createNode(link, ""));
                transactions.push(createRelationship(message['url'], link));
            }

            let statements = stackTransactions(transactions);
            console.log(statements);
            sendTransactions(statements);
        });
        console.log("Subscribed to Document Data");
    }
}