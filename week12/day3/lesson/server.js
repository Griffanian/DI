const express = require('express')

app = express()

app.use('/',express.static(__dirname +'/public'))


app.listen(3001, ()=>{
    console.log('run on port 3001')
})

app.get('/aboutme',(req,res) => {
    res.sendFile(__dirname + '/public/index.html')
})