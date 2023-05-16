const people = ["Greg", "Mary", "Devon", "James"];

people.shift()

people[2] = "Jason"

people.push("Miles")

const index = people.indexOf("Mary");

const copy = people.slice(1,3)

const index2 = people.indexOf("foo")

const index3 = people.length;

const last = people[index3-1]

for (const element of people) {
    console.log(element);
  }

  for (const element of people) {
    console.log(element);
    if (element === "Devon") {
        break
    }
  }