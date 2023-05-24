// Exercise 1
// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }

// const {name, location: {country, city, coordinates: [lat, lng]}} = person;

// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

// I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

//  Exercise 2 

// function displayStudentInfo(objUser){
//     const {first ,last} = objUser;
//     console.log('Your full name is ' + first + ' ' + last)
// }

// displayStudentInfo({first: 'Elie', last:'Schoppik'});

// Exercise 3 

// const users = { user1: 18273, user2: 92833, user3: 90315 }

// console.log(Object.entries(users))

// Exercise 4

// class Person {
//     constructor(name) {
//       this.name = name;
//     }
//   }
  
//   const member = new Person('John');
//   console.log(typeof member); 

// //   object

// Exercise 5

// 2

// Exercise 6

// 1. Both false as the '===' operator compares if these two are stored in the same place and as both are diffent arrays or object it returns false

//  2.

//4 as the object2 decleration create another reference to object one therfore when object1 is change object2 is changed
//4 again as object3 references object2 and object2 reference object1 
//5 by declaration

class Animal {
  constructor(name, type, color) {
    this.name = name;
    this.type = type;
    this.color = color;
  }
}

class Mammal extends Animal {
  sound(sound) {
    return `${sound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}. ${sound}`;
  }
}

const farmerCow = new Mammal('Lily', 'cow', 'brown and white');
const cowSound = farmerCow.sound("Moooo");

console.log(cowSound);