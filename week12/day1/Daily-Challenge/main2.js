const http = require("http");
const fs = require('fs').promises;
const { largeNumber } = require("./script");
const host = 'localhost';
const port = 3000;



const requestListener = function (req, res) {
    fs.readFile("index.html")
    .then(contents => {
        res.setHeader("Content-Type", "text/html");
        res.writeHead(200);
        res.end(contents + largeNumber + "<h1>Hi there at the frontend</h1>");
    })
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});