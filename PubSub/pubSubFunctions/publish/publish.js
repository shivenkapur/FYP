import databaseObjects from '../../configuration/databaseObjects.js';

export default async function publish(channel, message){

    const client = await databaseObjects.getClient();

    try{
        await client.publish(channel, message);
        return 'Published';
    } catch (error) {
        return 'Something went wrong! Could not publish.';
    }
}
