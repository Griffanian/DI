function makeAllCaps(arr) {
    let newArr = []
    let prom = new Promise(function(resolve,reject){
        const isString = (item) => typeof(item) === "string"
        if (arr.every(isString)){ 
            for (item of arr){
                newStr = item.charAt(0).toUpperCase() + item.slice(1)
                newArr.push(newStr)
            }
        }else {
            reject("array is not composed of strings.")
        }
        resolve(newArr)
    })
    return prom
}

function sortWords(arr){
    capitalised = true
    let prom = new Promise(function(resolve,reject){
        const isCapitalised = (item) => item.charAt(0) === item.charAt(0).toUpperCase()
        if (arr.length < 4){
            reject("array was less then 4 items")
        } else if (!arr.every(isCapitalised)) {
            reject("items were not capitalised")
        } else {
            resolve(arr.sort())
        }
    })
    return prom
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error))