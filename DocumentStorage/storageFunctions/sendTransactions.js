var request = require("request");

export default async function sendTransactions(statements, callback = (err,res) => {}){

    var txUrl = "http://localhost:7474/db/data/transaction/commit";

    request.post(
        {
            uri: txUrl,
            json: {
                statements: statements
            }
        },
        function(err,res) {
            callback(err,res);
        }
    );
}
