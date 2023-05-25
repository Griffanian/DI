function removeWhiteSpaces(arr){
    for (i=0; i < arr.length; i++){
        console.log(i,arr)
        if (arr[i] === ' '){
            delete arr[i]
        }
    }
    return arr
}
function charCounter(arr){
    countObj = {}
    for (let char of arr){
        if (Object.keys(countObj).includes(char)){
            countObj[char]+=1
        } else {
            countObj[char]=1
        }
    }
    return countObj
}
function objMaker(string){
    let array = [...string].filter(item => item !== ' ')
    let countObj = charCounter(array.sort())
    return countObj
}
function anagramChecker(string1,string2){
    countObj1=objMaker(string1.toLowerCase())
    countObj2=objMaker(string2.toLowerCase())
    
    if (JSON.stringify(countObj1) === JSON.stringify(countObj2)){
        return true
    } else {
        return false
    }
}

console.log(anagramChecker("Astronomer","Moon starer"))