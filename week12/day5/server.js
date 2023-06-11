express = require('express')
ejs = require('ejs')

const app = express()

app.set('view engine','ejs')

app.listen(process.env.PORT||3030, ()=>{
    console.log(`run on ${process.env.PORT||3030}`)
})

app.get('/',(req,res) =>{
    // res.send('hello')
    let login = true
    let user = {
        'firstName':'John',
        'lastName':'Doe',
    }
    res.render('index',{
        user
    })
})

// {
//     
// }