const express = require('express')
const {products} = require('./config/data.js')

const app = express()

const logger = (req,res,next) => {
    console.log('url=>',req.url)
    console.log('params=>',req.params)
    console.log('query=>',req.query)
    console.log('body=>',req.body)
    next()
}

app.use(logger)

app.use(express.urlencoded({extended:true}));
app.use(express.json())

app.listen(3001, () => {
    console.log('server is running on port 3001')
})



app.get('/api/products', (req,res) => {
    res.json(products)
})

app.get('/api/products/:id', (req,res) => {
    const id = req.params.id
    const product = products.find(item => item.id == id)
    if (!product){
        return res.status(404).json({message:'Product not found'})
    }
    res.status(200).json(product)
})

app.get('/api/search?', (req,res) => {
    nameChars = req.query.name
    const productFiltered = products.filter((item) => {
        return item.name.toLowerCase().includes(nameChars.toLowerCase())
    })
    if (productFiltered.length === 0){
         res.status(404).json({message:'Product not found'})        
    } else {
        res.send(productFiltered)
    }
})
app.post('/api/products', (req,res) => {
    products.push(req.body)
    res.status(201).json(products)
})

app.delete('/api/products/:id', (req,res) => {
    const id = req.params.id
    const index = products.findIndex(item => item.id === id)
    if (id === -1){
         res.status(404).json({message:'Product not found'})        
    } else {
        products.splice(index,1)
    }
    res.status(200).json(products)
})

app.put('/api/products/:id', (req,res) => {
    const id = req.params.id
    const index = products.findIndex(item => item.id === id)
    if (id === -1){
         res.status(404).json({message:'Product not found'})        
    } else {
        products[index] = {
            ...products[index],
            "name":req.body.name,
            "price":req.body.price
        }
    }
    res.send(req.body,products[index])
})