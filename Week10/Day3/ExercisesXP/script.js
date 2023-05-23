// Exercise 1

// ------1------
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);

// ['bread', "apple", "orange", 'chicken', "carrot", "potato"] as the spread operator continues the list

// ------2------
// const country = "USA";
// console.log([...country]);

// ['U', 'S', 'A'] as will spread the list into a string

// Exercise 2 

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

const helloArray = users.map((elem) => 'Hello '+ elem.firstName)

const fullArray = users.filter((elem) => elem.role === 'Full Stack Resident')

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

// Exercise 3

const newString = epic.reduce(function (accumulator, word) {return accumulator + ' ' + word;}, "");

// Exercise 4

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];

const passedArray = students.filter(function(elem) {return elem.isPassed === true})

console.log(passedArray)