export default function stackTransactions(transactions){

    let statements = [];
    for(let transactionIndex in transactions){
        let transaction = transactions[transactionIndex];
        statements.push(transaction);
    }

    return statements;
}

