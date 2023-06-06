// Exercise 1

// fs = require('fs')

// fs.readFile('example.txt','utf-8' ,function(err,data){
//     if (err){
//         console.error(err)
//         return
//     }
//     console.log(data);
// });

// Exercise 2 

fs = require('fs')


const content = 'Some Text To See'

fs.writeFile('newExample.txt',content, (err) => {
    if (err){
        console.error(err);
        return;
    } 
    console.log('File created successfully!');
})


const additionalContent = '\nThis is additional content to append.';

fs.appendFile('newExample.txt', additionalContent, (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Content appended successfully!');
  });

fs.unlink('newExample.txt', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('File deleted successfully!');
  });