// Exercise 1

// const express = require("express");
// const cors = require("cors");

// const app = express()

// app.use(cors());

// app.get('/',(req,res) => {
// const user = {
//     firstname: 'John',
//     lastname: 'Doe'
// }
// res.send(JSON.stringify(user))
// })

// app.listen(3000, () => {
// console.log('Server is running on port 3000');
// });

// Exercise 2

// const handler = (req,res,next) => {    
//     next()
// }

// const express = require("express");
// const cors = require("cors");

// const app = express()

// app.use(cors());
// app.use(handler)
// app.get('/:id',(req,res) => {
//     const id = req.params.id
//     console.log({'id':id})
//     res.send({'id':id})
// })

// app.listen(3000, () => {
// console.log('Server is running on port 3000');
// });

// Exercise 3

const handler = (req,res,next) => {    
    next()
}

const express = require("express");
const cors = require("cors");

const app = express()

app.use(cors());
app.use(handler)
app.use(express.static('public'))

app.get('/',(req,res) => {
})

app.listen(3000, () => {
console.log('Server is running on port 3000');
});