div = document.getElementById("navBar")
div.id = "socialNetworkNavigation"

unorderedList = document.querySelector("ul")
newListItem = document.createElement("li")
unorderedList.appendChild(newListItem)
let textNode = document.createTextNode("Logout")
newListItem.appendChild(textNode)

console.log(unorderedList.firstElementChild.firstChild.textContent)
console.log(unorderedList.lastElementChild.firstChild.textContent)

