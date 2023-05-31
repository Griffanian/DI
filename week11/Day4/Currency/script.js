currenciesArray = JSON.parse(currencies)
var convertHasRun = false
for (item of currenciesArray){
    let code = item["Currency Code"]
    let curName = item["Currency Name"]
    const newOption = document.createElement("option")
    newOption.value = code + " - " + curName
    newOption.textContent = code + " - " + curName
    const newOptionClone = newOption.cloneNode(true)
    document.getElementById("fcurrrency").appendChild(newOption)
    document.getElementById("scurrrency").appendChild(newOptionClone)
}

async function getData(url){
    let responce = await fetch(url)
    if (responce.ok){
        let data = await responce.json()
        return data;
    } else {
        return responce
    } 
}

async function convert(event){
    event.preventDefault()

    const myForm = document.forms["myForm"]

    const fcurrency = myForm["fcurrrency"].value.split(" - ")
    const fcurrencyCode = fcurrency[0]

    const scurrency = myForm["scurrrency"].value.split(" - ")
    const scurrencyCode = scurrency[0]

    let amount = parseFloat(myForm["Amount"].value).toFixed(2)

    let data = await getData(`https://v6.exchangerate-api.com/v6/e2fad6924ddcdbf90b807053/latest/${fcurrencyCode}`)
    let rate = data["conversion_rates"][scurrencyCode]
    let converted = (amount*rate).toFixed(2)

    result = document.getElementById("result")
    result.innerHTML = `${amount} ${fcurrency[1]} <p> = </p> ${converted} ${scurrency[1]}`
    convertHasRun = true
}

function switchCur(){
    const myForm = document.forms["myForm"]
    const fcurrency = myForm["fcurrrency"].value
    const scurrency = myForm["scurrrency"].value
    myForm["fcurrrency"].value = scurrency
    myForm["scurrrency"].value = fcurrency
    if (convertHasRun){
        convert(event)
    }
}
