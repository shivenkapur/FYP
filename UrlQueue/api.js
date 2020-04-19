import addUrl from './redisFunctions/addUrl/addUrl.js';
import removeUrls from './redisFunctions/removeUrls/removeUrls.js';
import getUrls from './redisFunctions/getUrls.js';

export default {
    addUrl: async function (url){
        addUrl(url);
    },
    removeUrls: async function (){
        removeUrls();
    },
    getUrls: async function (key){
        getUrls(key);
    }
}