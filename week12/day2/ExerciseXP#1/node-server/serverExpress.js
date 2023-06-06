const express = require('express')

const app = express()

app.use(express.urlencoded({extended:true}))
app.use(express.json())

app.listen(3000,() => {
    console.log('server is running on port 3000')
})

app.get('/',(req,res) => {
    res.end("<h1>This is an HTML tag</h1>")
})