let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = () => {
  groceries.fruits.forEach(fruit => {
    console.log(fruit);
  });
};

const cloneGroceries = () => {
  user = client
  client = 'Betty' //this will not also change user as user is linked to the global client not the local
  shopping = groceries
  groceries.totalPrice = '35$'// this will change shopping as modifying an element of the global object will affect its clone
  groceries.payed = false// this is the same as the previous
}

cloneGroceries()