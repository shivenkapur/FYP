import addUrlRoute from './routes/addUrlRoute.js';
import removeUrl from './routes/removeUrlRoute.js';
import getAllKeysRoute from './routes/getAllKeysRoute.js';
import getAllUrlsRoute from './routes/getAllUrlsRoute.js';

import bodyParser from 'body-parser';

const express = require('express');
const app = express();
const port = 8000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/addUrl', addUrlRoute);
app.use('/removeUrl', removeUrl);
app.use('/getAllKeys', getAllKeysRoute);
app.use('/getAllUrls', getAllUrlsRoute);

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))