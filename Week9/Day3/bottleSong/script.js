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
    console.log("We have " + bottlesChange + " bottles of beer on the wall");
    if (i == 1) {
        console.log("Take _1_ down, pass it around");
    } else {
        console.log("Take _" + i + "_ down, pass them around");
    }
    bottlesChange -= i;
    if (bottlesChange === 0){
        console.log("We now have no bottles");
        break
    } else {
        console.log("We now have " + bottlesChange + " bottles");
    }
}