import getAllLinksRoute from './routes/getAllLinksRoute.js';
import getAllMetaDataRoute from './routes/getAllMetaDataRoute.js';

const express = require('express');
const app = express();
const port = 3000;

app.use('/getAllLinks', getAllLinksRoute);
app.use('/getAllMetaData', getAllMetaDataRoute);

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))