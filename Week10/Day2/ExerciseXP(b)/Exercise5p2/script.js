
function makeJuice(size = 'small') {

    let sizes = ['small','medium','large']
    let ingredients = [];

    function addIngredients(ingredient1 = 'banana',ingredient2 = 'strawberry',ingredient3 = 'milk'){
        ingredients.push([ingredient1,ingredient2,ingredient3])
    }
    function displayJuice(ingredientList = ['banana','strawberry','milk']){
        console.log(`The client wants a ${size} juice, containing ${ingredientList[0]}, ${ingredientList[1]}, ${ingredientList[2]}`)
    }
    
    if (sizes.includes(size) === true){
        addIngredients()
        addIngredients('lime', 'mango', 'chocolate')
        ingredients.forEach(displayJuice)
    } else {
        console.log("That is not a size option")
    }
}
makeJuice()

