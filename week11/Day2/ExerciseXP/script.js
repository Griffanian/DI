// Exercise 1

// function compareToTen(num){
//     let promise = new Promise(function (resolve, reject) {
//         if (num <= 10) {
//             resolve(num + " is a number less than 10");
//         } else {
//             reject(num + " number is greater than 10");
//         }
//     }); 
//     return promise
// }

// compareToTen(8)
// .then(result => console.log(result))
// .catch(error => console.log(error))

// Exercise 2 

// 1.

// let success = new Promise(function (resolve, reject) {
//     setTimeout(() => resolve("success"), 4000);
// });
// success.then((successResult) => console.log(successResult))

// 2.

// setTimeout(() => Promise.resolve("Success")
// .then(value => console.log(value))
// .catch(error => console.log("Ooops something went wrong")), 4000)

// Exercise 3

// const resolvPro = Promise.resolve(3)
// const rejectPro = Promise.reject("Boo!")

