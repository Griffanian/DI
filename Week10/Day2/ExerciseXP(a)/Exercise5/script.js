const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["st","nd","rd","th"];

for (let i=1; i < colors.length+1; i++) {
    choice = i > 3 ? i + ordinal[3] +" choice is " + colors[i-1] : i + ordinal[i-1] +" choice is " + colors[i-1]
    console.log(choice)
}