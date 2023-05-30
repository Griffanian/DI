

// Exercise 1

// fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
// .then(responce => {
//     if (!responce.ok){
//         throw new Error(`HTTP error! Status: ${response.status}`);
//     }
//     return responce.json()
// })
// .then(data=> console.log(data))
// .catch(err => console.log(err))

// Exercise 2


// fetch("https://api.giphy.com/v1/gifs/search?q=suns&limit=10&offset=2&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
// .then(responce => {
//     if (!responce.ok){
//         throw new Error(`HTTP error! Status: ${response.status}`);
//     }
//     return responce.json()
// })
// .then(data=> console.log(data))
// .catch(err => console.log(err))

// Exercise 3

// async function getFile(url){
//     let responce = await fetch(url)
//     if (!responce.ok){
//         throw new Error(`HTTP error! Status: ${response.status}`);
//         }
//     let data = await responce.json()
//     console.log(data);
// }

// getFile("https://api.giphy.com/v1/gifs/search?q=suns&limit=10&offset=2&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")

// Exercise 4
// calling
// resolved
// as asyn function will await the resoloution of a promise