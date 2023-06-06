const express = require("express");
const cors = require("cors");

const app = express()

app.use(cors());

app.use(express.urlencoded({extended:true}))
app.use(express.json())

app.get('/aboutMe/:hobby',(req,res) => {
    const hobby = req.params.hobby
    if (typeof(hobby)=== "string"){
        res.send(`<p>${hobby}</p>`)
    } else {
        res.status(404).json({message:'type not allowed'})
    }
})

app.get('/pic',(req,res) => {
    res.send(`<img src="https://images.unsplash.com/photo-1685443930058-877ab44b526c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1064&q=80" alt="Girl in a jacket" width="500" height="600"></img>`)
})

app.get('/form',(req,res) => {
    res.sendFile('public/index.html',{root: __dirname })
})

app.post("/formdata", (req, res) => {
   const email = req.body.
   res.send(email)

});

app.listen(3000, () => {
console.log('Server is running on port 3000');
});