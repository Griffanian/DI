const user = {
    firstname: 'John',
    lastname: 'Doe'
}

const http = require('http')

const server = http.createServer((req, res) => {
    res.write(JSON.stringify(user))
    res.end() 
  });
  

  server.listen(8080, () => {
    console.log(`Server running at http://localhost:8080/`);
  });
 
  
  