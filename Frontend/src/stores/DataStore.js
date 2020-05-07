import { EventEmitter } from "events";

class DataStore extends EventEmitter {
  constructor() {
    super();
  }

  setUrls(nodeId, urls) {
    localStorage.setItem('urls-' + nodeId, urls);
  }

  getUrls(nodeId){
    return localStorage.getItem('urls-' + nodeId);
  }

  selectedNodeChanged(nodeId) {
    this.getUrls.setUrls(nodeId, [
      {
        url: "https://www.google.com",
        metaData: "Wtf brooooo"
      },
      {
        url: "https://www.google.com",
        metaData: "Wtf brooooo"
      },
      {
        url: "https://www.google.com",
        metaData: "Wtf brooooo"
      }
    ])
    this.emit("selectedNodeChanged", nodeId);
  }
}

const dataStore = new DataStore();
export default dataStore;
