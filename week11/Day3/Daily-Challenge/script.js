async function getGifId(keyword){
    let responce = await fetch(`https://api.giphy.com/v1/gifs/search?q=${keyword}&limit=1&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
    if (!responce.ok){
        throw new Error(`HTTP error! Status: ${response.status}`);
        }
    let data = await responce.json()
    const id = data['data'][0]['id']
    return id;
}

function deleteGif(id){
    const button = document.getElementById(id)
    const gifBox = button.parentNode
    gifBox.remove()
}
function deleteAll(){
    let gifBoxes = document.querySelectorAll(".gifBox")
    gifBoxes.forEach(function(element) {
        element.remove()
    });
}
async function addGif(event){
    event.preventDefault();

    let form =  document.forms["newGifForm"];
    keyword = form["search"].value
    form.reset()

    const gifId = await getGifId(keyword)

    const container = document.getElementById("container")

    let gifBox = document.createElement("div")
    gifBox.classList.add("gifBox")
    container.appendChild(gifBox)

    const newIframe = document.createElement("iframe")
    newIframe.src = "https://giphy.com/embed/" + gifId
    gifBox.appendChild(newIframe)

    let frames = document.getElementsByTagName("iframe")

    const newButton = document.createElement("button")
    newButton.id = 'button' + frames.length
    newButton.setAttribute("onclick","deleteGif(this.id)")
    newButton.textContent = "delete"

    gifBox.appendChild(newButton)
}
