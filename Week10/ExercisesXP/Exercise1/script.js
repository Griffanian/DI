const article = document.body.firstElementChild;
const firstHeader = article.firstElementChild;
console.log(firstHeader)

const lastPara = document.querySelector("article p:last-child")
lastPara.remove()

function h2Click() {
    const header2 = document.getElementsByTagName("h2")[0]
    header2.style.backgroundColor = "red";
}
document.getElementsByTagName("h2")[0].addEventListener("click",h2Click);

function h3Click() {
    const header3 = document.getElementsByTagName("h3")[0]
    header3.style.display = "none"
}
document.getElementsByTagName("h3")[0].addEventListener("click",h3Click);

function makeParaBold() {
    var css = 'p {font-weight: bold;}',
    head = document.head || document.getElementsByTagName('head')[0],
    style = document.createElement('style');
    
    head.appendChild(style);

    if (style.styleSheet){
        style.styleSheet.cssText = css;
    } else {
        style.appendChild(document.createTextNode(css));
}
}
