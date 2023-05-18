function askNumber(){
    while (true) {
        let userInput = prompt("Please enter a number to count down from in the song");
        if (userInput === null) {
            break
        } else {
            if (userInput === '' || isNaN(userInput)) {
                alert("Sorry Not a number, Goodbye");
            } else{
                num = parseInt(userInput);
                return num
            }
            break;
        }
    }
}
bottlesStart = askNumber()
bottlesChange = bottlesStart
console.log(bottlesStart)
console.log(bottlesChange)
for (let i = 1; i <= bottlesStart; i++) {
    if (bottlesChange === 1) {
        console.log("We have 1 bottle of beer on the wall");
    } else {
        console.log("We have " + bottlesChange + " bottle of beer on the wall");
    }
    
    if (i === 1) {
        console.log("Take _1_ down, pass it around");
    } else {
        console.log("Take _" + i + "_ down, pass them around");
    }
    bottlesChange -= i;
    if (bottlesChange === 0){
        console.log("We now have no bottles");
        break
    } else if (bottlesChange === 1) {
        console.log("We now have 1 bottle");
    } else {
        console.log("We have " + bottlesChange + " bottle of beer on the wall");
    }
}