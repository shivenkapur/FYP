import createNode from './storageFunctions/createNode/createNode.js';
import createRelationship from './storageFunctions/createRelationship/createRelationship.js';
import getNodes from './storageFunctions/getNodes/getNodes.js';
import stackTransactions from './storageFunctions/stackTransactions.js';
import sendTransactions from './storageFunctions/sendTransactions.js';

async function start(){

  let statements = stackTransactions([createNode("14"), createRelationship("13", "12")]);
  console.log(statements)
  sendTransactions(statements);

}

start()

