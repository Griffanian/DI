(function (userName) {
    navBar = document.getElementById("navbarSupportedContent")

    newDiv = document.createElement("div")

    picDiv = document.createElement("img")
    picDiv.src = 'https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHNxdWFyZSUyMHByb2ZpbGV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=1000&q=60'
    picDiv.width = 70
    picDiv.style.border = 'solid 1px black;'
    picDiv.style.borderRadius = '50%' 

    newDiv.appendChild(picDiv)
    
    newPara = document.createElement("p")
    newPara.textContent = "random guy"
    newDiv.appendChild(newPara)

    navBar.appendChild(newDiv)
})('bob');