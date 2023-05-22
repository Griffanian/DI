function toGrams1(weight) {
    return weight*1000
}
const toGrams2 = function(weight) {
    return weight*1000
}

// the function exression is not hoisted therefore it can only be called after it is defined

const  toGrams3 = (weight) => weight*1000

toGrams3(2)