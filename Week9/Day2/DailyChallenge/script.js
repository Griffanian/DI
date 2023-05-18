class Planet {
    static instances =[]
    static colors = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "magenta", "black", "white"];
    constructor(name){
        this.name = name
        const randomIndex = Math.floor(Math.random() * Planet.colors.length);
        this.color = Planet.colors[randomIndex];
        this.moons = []
        Planet.instances.push(this)
    }
}
function checkName(array,name){
    for (obj of array){
        if (array.name === name){
            return true
        }
    }
}

function getPlanet(array,name){
    for (obj of array){
        if (obj.name === name){
            return obj
        }
    }
}

class Moon {
    constructor(name,planet){
        this.name = name
        const randomIndex = Math.floor(Math.random() * Planet.colors.length);
        this.color = Planet.colors[randomIndex]
        this.planet = planet
        const allowed = checkName(Planet.instances,planet)
        const planetObj = getPlanet(Planet.instances,planet)

        if (allowed === true) {
            console.log("Cannot add moons to " + planet + " as not yet in the database")
        } else {
            planetObj.moons.push(this)
        }
    }
}

article = document.getElementsByClassName("listPlanets")[0]

planet1 = new Planet("Mercury")
planet2 = new Planet("Venus")
planet3 = new Planet("Earth")
planet4 = new Planet("Mars")
planet5 = new Planet("Jupiter")
planet6 = new Planet("Saturn")
planet7 = new Planet("Uranus")
planet8 = new Planet("Neptune")
planet9 = new Planet("Pluto")

moon1 = new Moon("Moon","Earth")
moon2 = new Moon("Phobos", "Mars")
moon3 = new Moon("Deimos", "Mars")

moon4 = new Moon("Io", "Jupiter")
moon5 = new Moon("Europa", "Jupiter")
moon6 = new Moon("Ganymede", "Jupiter")
moon7 = new Moon("Callisto", "Jupiter")

moon8 = new Moon("Titan", "Saturn")
moon9 = new Moon("Enceladus", "Saturn")
moon10 = new Moon("Iapetus", "Saturn")
moon11 = new Moon("Rhea", "Saturn")
moon12 = new Moon("Dione", "Saturn")

moon13 = new Moon("Miranda", "Uranus")
moon14 = new Moon("Ariel", "Uranus")
moon15 = new Moon("Umbriel", "Uranus")
moon16 = new Moon("Titania", "Uranus")
moon17 = new Moon("Oberon", "Uranus")

moon18 = new Moon("Triton", "Neptune")
moon19 = new Moon("Nereid", "Neptune")

moon20 = new Moon("Charon", "Pluto")
moon21 = new Moon("Styx", "Pluto")
moon22 = new Moon("Nix", "Pluto")
moon23 = new Moon("Kerberos", "Pluto")
moon24 = new Moon("Hydra", "Pluto")

for (let object of Planet.instances) {

    newSection = document.createElement("section")
    newSection.classList.add("planet")
    newSection.classList.add(object.name)
    newSection.style.cssText = `background-color: ${object.color};`
    article.appendChild(newSection)
    console.log(object.moons)
    for (let [index, moonObj] of object.moons.entries()){
        newDiv = document.createElement("div")
        newDiv.classList.add("moon")
        newDiv.classList.add(moonObj.name)
        newDiv.style.cssText = `background-color: ${moonObj.color}; margin-left: ${index*40}px;`
        console.log([index, moonObj])
        article.appendChild(newDiv)
    }
}
