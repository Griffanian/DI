fs = require('fs')

let score = 0;
let breaker = false;

fs.readFile('Right-Left_Week7JS/RightLeft.txt','utf-8', function(err,data){
    if (err){
        console.error(err)
        return
    }
    dataArr = data.split('');
    console.log(dataArr)
    for (let i = 0; i < dataArr.length; i++){
        const item = dataArr[i]; 
        if (item === '>'){
            score+=1
        } else if (item === '<'){
            score-=1
        }
        if (breaker === false && score ===-1){
            console.log(i)
            breaker = true
        }
        
    }
    console.log(score + ' steps to the right.');
    
});