const http = require("http");
const fs = require('fs').promises;
const { largeNumber } = require("./script");
const host = 'localhost';
const port = 3000;

var currentDateTime = new Date();

var OfWeek = currentDateTime.getDay();
var days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
var dayName = days[OfWeek];

var month = currentDateTime.getMonth()
var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
var monthName = months[month]

var date = currentDateTime.getDate()

var year = currentDateTime.getFullYear()

var time = currentDateTime.toLocaleTimeString()

var timeZone = currentDateTime.getTimezoneOffset()
const requestListener = function (req, res) {
    res.setHeader("Content-Type", "text/html");
    res.writeHead(200);
    res.end(`<p>The date and time are currently: 
    ${dayName} 
    ${monthName} 
    ${date} 
    ${year} 
    ${time} 
    GMT+${-timeZone/60}(Israel Daylight Time)</p>`);

};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});