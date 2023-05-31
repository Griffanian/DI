const loaderDiv = document.getElementById("loader")
loaderDiv.style = "display: none;"
const notFound = document.getElementById("notFound")
notFound.style = "display: none;"

async function getData(url){
    let responce = await fetch(url)
    if (responce.ok){
        let data = await responce.json()
        return data;
    } else {
        return responce
    } 
}

async function getRandomPerson(){
    const randomNum = Math.floor(Math.random()*83)+1
    let url =  `https://www.swapi.tech/api/people/${randomNum}`
    data = await getData(url)
    try{
        return data["result"]["properties"];
    } catch {}
    
}
function startLoader(){
    const content = document.getElementById("content")
    content.style = "display: none;"
    loaderDiv.style = "display:block"
}
function finishLoader(){
    const content = document.getElementById("content")
    content.style = "display:block"
    loaderDiv.style = "display:none"
}
function startError(){
    const content = document.getElementById("content")
    content.style = "display: none;"
    notFound.style = "display:block"
}
function finishError(){
    const content = document.getElementById("content")
    content.style = "display:block"
    notFound.style = "display: none;"
}
async function updatePage(){
    finishError()
    startLoader()
    const personObj = await getRandomPerson()
    try{
        const data = await getData(personObj["homeworld"])
    const home_world = data["result"]["properties"]["name"]
    document.getElementById("name").textContent = "Name: " + personObj["name"]
    document.getElementById("height").textContent = "Height: " + personObj["height"]
    document.getElementById("gender").textContent = "Gender: " + personObj["gender"]
    document.getElementById("birth-year").textContent = "Birth Year: " + personObj["birth_year"]
    document.getElementById("home-world").textContent = "Home World: " + home_world
    finishLoader()
    }
    catch{
        finishLoader()
        startError()
    }
    
}