const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];

let usernames = []
function addToArray (obj) {
    usernames.push(obj['username'] + '!')
    console.log(usernames)
}

function addWinner(obj) {
    if (obj['score'] > 5) {
        usernames.push(obj['username'])
    }
}

// gameInfo.forEach(addToArray)
// gameInfo.forEach(addWinner)

// console.log(usernames)

var score = 0

function addToScore(obj){
    score +=obj['score']
}

// gameInfo.forEach(addToScore)

// console.log(score)