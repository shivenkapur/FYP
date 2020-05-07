import pubsub from 'pubsub';

export default {
    getClusters: async function(){
        
        pubsub.subscribe("clusterDocuments", async (channel, message) => {
            let data = JSON.parse(message);

            console.log(data)
            for(let dataIndex in data){
                let dataPoint = data[dataIndex];
                console.log(dataPoint.row, dataPoint.meta);
            }

        });
        console.log("Subscribed to Cluster Documents");
    },
}