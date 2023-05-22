function makeJuice(size = 'small') {
    sizes =['small','medium','large']
    function addIngredients(ingredient1 = 'banana',ingredient2 = 'strawberry',ingredient3 = 'milk'){
        console.log(`The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}`)
    }
    if (sizes.includes(size) === true){
        addIngredients()
    } else {
        console.log("That is not a size option")
    }
}

makeJuice()