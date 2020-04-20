import createNode from './routes/createNodeRoute.js';
import createRelationship from './routes/createRelationshipRoute.js';
import getNodes from './routes/getNodesRoute.js';

import bodyParser from 'body-parser';

const express = require('express')
const app = express()
const port = 5000

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/createNode', createNode);
app.use('/createRelationship', createRelationship);
app.use('/getNodes', getNodes);

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))