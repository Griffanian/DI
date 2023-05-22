function firstFunc() {
    alert("Hello World")
}
// const firstTimeout = setTimeout(firstFunc, 2000);

function secondFunc() {
    container = document.getElementById("container")
    para = document.createElement("p")
    para.textContent = "Hello World"
    container.appendChild(para)
}
// const secondTimeout = setTimeout(secondFunc, 2000);

function thirdFunc() {
    secondFunc()
}
const intervalId = setInterval(thirdFunc,2000)
setTimeout(function(){
    clearInterval(intervalId)
},10000)
