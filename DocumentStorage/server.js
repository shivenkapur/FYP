const express = require('express')
const app = express()
const port = 5000

app.use('/createNode', createNode);
app.use('/createRelationship', createRelationship);
app.use('/getNodes', getNodes);

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))