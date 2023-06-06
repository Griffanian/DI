const http= require('http')
const server = http.createServer((req, res) => {
    res.write('<h1>This is my first responce</h1>');
    res.write('<h1>This is my second responce.</h1>');
    res.write('<p>This is my third responce</p>');
  
    res.end(); 
  });
  

  server.listen(3001, () => {
    console.log(`Server running at http://localhost:3001/`);
  });
 
  
  
  
  
  
  