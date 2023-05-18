function askNumber(){
    while (true) {
        let userInput = prompt("Please enter a number between 0 and 10.");
        if (userInput === null) {
            break
        } else {
            if (userInput === '' || isNaN(userInput)) {
                alert("Sorry Not a number, Goodbye");
            } else if (userInput < 0 || userInput > 10) {
                alert("Sorry it's not a good number, Goodbye");
            } else{
                num = parseInt(userInput);
                return num
            }
            break;
        }
    }
}

function getRandomNumber(min, max) {
    const randomDecimal = Math.random();
    const randomNumber = Math.floor(randomDecimal * (max - min + 1)) + min;
    return randomNumber;
  }

function compareNumbers(userNumber,computerNumber) {
    if (userNumber > computerNumber){
        return "Your number is bigger than the computers"
    } else if (userNumber < computerNumber) {
        return "Your number is smaller than the computers"
    } else if (userNumber === computerNumber){
        return "Winner. Well done"
    } else {
        return "You canceled. Goodbye"
    }
}

function playTheGame(){
    let text = "Would you like to play a game?\nEither OK or Cancel."
    if (confirm(text) == true){
        const computerNumber = getRandomNumber(0,10)
        
        for (let i = 1; i <= 3; i++) {
            const userNumber = askNumber()
            compareResult = compareNumbers(userNumber,computerNumber)
            alert(compareResult)
            if (compareResult === "Winner. Well done" || compareResult === "You canceled. Goodbye") {
                break
            } if (i === 3) {
                alert("You are out of chances! Goodbye.")
            }
        }
        

    } else {
        alert("No problem, Goodbye")
    }
}
