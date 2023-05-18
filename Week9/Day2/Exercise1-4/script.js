// Exercise 1 

function isDivisible(divisor){
  sum = 0
  for (let i = 0; i < 501; i++){
    if (i % divisor === 0) {
      console.log(i)
      sum += i
    }
  }
  console.log(sum)
}
// isDivisible()

// Exercise 2

const stock = { 
  "banana": 6, 
  "apple": 3,
  "pear": 12,
  "orange": 32,
  "blueberry":1
}  

const prices = {    
  "banana": 4, 
  "apple": 2, 
  "pear": 1,
  "orange": 1.5,
  "blueberry":10
} 

shoppingList = ["banana", "orange", "apple"]

function myBill(){
  let total = 0
  for (let element of shoppingList){
    if (element in stock){
      total += prices[element]
      stock[element] -=1
    }
  }
  return total
}

// myBill()

// Exercise 3

function changeEnough(itemPrice, amountOfChange){
  let changeSum = 0.00
  changeSum += 
   amountOfChange[0]*0.25 +
   amountOfChange[1]*0.1 +
   amountOfChange[2]*0.05 +
   amountOfChange[3]*0.01
  if (itemPrice < changeSum){
    return true
  }
  else{
    return false
  }
}

// console.log(changeEnough(0.75, [0,0,20,5]))

// Exercise 4 

function hotelCost() {
  var nights = 0;
  var costPerNight = 140;
  
  while (true) {
    var userInput = prompt("Enter the number of nights you would like to stay:");
    
    if (userInput === null || isNaN(userInput)) {
      alert("Please enter a valid number of nights.");
    } else {
      nights = parseInt(userInput);
      break;
    }
  }
  
  var totalCost = nights * costPerNight;
  return totalCost;
}

function planeRideCost() {
  let price = 0
  while (true) {
      var userInput = prompt("Enter your destination: ")
      if (userInput === null || typeof userInput !== 'string') {
          alert("Please enter a valid destination");
      } else if (userInput === "London") {
          price += 183
          break
      } else if (userInput === "Paris") {
          price += 220
          break
      } else {
          price += 300;
          break
      }

  }
  return price
}

function rentalCarCost(){
  var days = 0;
  var costPerDay = 40;
  multiplier = 1
  
  while (true) {
    var userInput = prompt("Enter the number of days you would like rent the car:");
    
    if (userInput === null || isNaN(userInput)) {
      alert("Please enter a valid number of days.");
    } else {
      days = parseInt(userInput);
      break;
    }
  }

  if (days > 10) {
      multiplier = 0.95
  }
  var totalCost = days * costPerDay * multiplier;
  return totalCost;
}

function totalVacationCost() {
  totalPrice = 0 
  totalPrice += hotelCost() + planeRideCost() + rentalCarCost()
  alert("The hotel cost is : $" + hotelCost() +
   "\nThe plane cost is : $" + planeRideCost() +
   "\nThe rental cost is : $" + rentalCarCost() +
   "\nThe total cost is : $" + totalPrice);
}

// totalVacationCost()


