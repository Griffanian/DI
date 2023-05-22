let allBoldItems;

function getBold_items() {
    boldItem = document.querySelectorAll("strong")
    allBoldItems = boldItem
}

function highlight() {
    for (let item of allBoldItems) {
        item.style.color = "blue"
    }
}

function returnNormal() {
    for (let item of allBoldItems) {
        item.style.color = "black"
    }
}
getBold_items()
for (let item of allBoldItems) {
    item.addEventListener("mouseover", highlight)
    item.addEventListener("mouseout", returnNormal)
}