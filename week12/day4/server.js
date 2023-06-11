const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const path = require('path')

const app = express();

app.use(express.static('public'))

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true })); 

const db = require('knex')({
    client: 'pg',
    connection: {
        host: '127.0.0.1',
        user: 'postgres',
        password: '1234',
        database: 'user',
        port: 5432
    }
});

app.set("db", db);

function addUser(obj){
    // const hashedPassword = bcrypt.hashSync(obj.password, 10);
    db('users')
        .insert({
            'fname':obj.fname,
            'lname':obj.lname,
            'email':obj.email,
            'username':obj.username,
            'password': obj.password})
        .returning('*')
}

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + 'public/index.html'))
});

app.post('/user', (req, res) => {
    res.send(req.body);
    addUser(req.body)
    // .then(data => {
    //     res.send({message:'OK'})
    // }).catch(err => {
    //     res.send({message:err.detail})
    //   })
});

app.listen(3000, () => console.log('listening on port 3000!'));