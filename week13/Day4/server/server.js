const express = require('express')
const cors = require('cors')
var bodyParser = require('body-parser')

const app = express()

app.use(express.urlencoded({extended:true}))
app.use(express.json())

app.use(cors());

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.get('/api/hello',(req,res) => {
    res.send('Hello From Express')
})

app.post('/api/world',(req,res) => {
    console.log(JSON.stringify(req.body))
    const resStr = "I received your POST request. This is what you sent me: " + req.body
    res.send(resStr)
})

app.listen(3030,() => {
    console.log('server is running on port 3030')
})