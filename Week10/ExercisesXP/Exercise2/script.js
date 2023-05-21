frm = document.forms[0]
console.log(frm)

const fnameInputId = document.getElementById("fname")
const lnameInputId = document.getElementById("lname")
console.log(fnameInputId)
console.log(lnameInputId)

const fnameInput = document.getElementsByName("fname")[0]
const lnameInput = document.getElementsByName("lname")[0]
console.log(fnameInput)
console.log(lnameInput)

frm.addEventListener('submit',function (event){
    event.preventDefault();

    const fnameValue = fnameInput.value
    const lnameValue = lnameInput.value

    if (fnameValue != '' && lnameValue != '') {
        usersAnswer = document.getElementsByClassName("usersAnswer")[0]

        newListItem = document.createElement("li")
        newListItem.textContent = fnameValue + ' ' +lnameValue

        usersAnswer.appendChild(newListItem)
    }
    
    frm.reset()
}) 

