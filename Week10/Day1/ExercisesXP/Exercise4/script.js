frm = document.forms[0]

frm.addEventListener('submit',function (event){
    event.preventDefault();


    const radiusInput = document.getElementById("radius")
    const radiusInt = parseInt(radiusInput.value)

    if (Number.isInteger(radiusInt)) {
        output = document.getElementById("output")
        const pi = 3.141592653
        volume = 4/3*pi*(radiusInt)**3
        output.textContent = "volume is " + volume + "m^3"
    } else {
        alert("please enter an integer")
        frm.reset()
    }    
}) 