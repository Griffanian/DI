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
    console.log(bottlesChange + " " + (bottlesChange === 1 ? "bottle" : "bottles") + " of beer on the wall");
    console.log(bottlesChange + " " + (bottlesChange === 1 ? "bottle" : "bottles") + " of beer");
    console.log("Take _" + (i > bottlesChange ? bottlesChange : i) + "_ down, pass " + (i === 1 ? "it" : "them") + " around");
    bottlesChange -= i;
    console.log("We now have " + (bottlesChange > 0 ? bottlesChange : "no") + " " + (bottlesChange === 1 ? pluralBottles : "bottle"));
    if (bottlesChange <= 0){
        break
    }
}