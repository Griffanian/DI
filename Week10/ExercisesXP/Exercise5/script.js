div = document.getElementsByTagName("div")[0]

function click() {
    currentWidth = div.offsetWidth
    div.style.width = currentWidth + 30 + 'px'
    currentHeight = div.offsetHeight
    div.style.height = currentHeight + 30 + 'px'
}

function doubleClick() {
    currentWidth = div.offsetWidth
    newWidth = currentWidth - 90
    div.style.width = newWidth + 'px'
    div.style.height = newWidth + 'px'
    console.log("worked")
}

function hover() {
    div.style.backgroundColor = 'rebeccapurple'
}

function unHover() {
    div.style.backgroundColor = 'red'
}


document.getElementsByTagName("div")[0].addEventListener("click",click);
document.getElementsByTagName("div")[0].addEventListener("mouseover",hover);
document.getElementsByTagName("div")[0].addEventListener("mouseout",unHover);
document.getElementsByTagName("div")[0].addEventListener("dblclick",doubleClick);