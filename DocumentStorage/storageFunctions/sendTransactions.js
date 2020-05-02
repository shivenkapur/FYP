var request = require("request");

export default async function sendTransactions(statements){

    var txUrl = "http://localhost:7474/db/data/transaction/commit";

    request.post(
        {
            uri: txUrl,
            json: {
                statements: statements
            }
        },
        function(err,res) {
            console.log(res.body)
        }
    );
}
