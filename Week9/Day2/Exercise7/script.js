class Book {
    static instances =[]
    constructor(title,author,image) {
        this.title = title
        this.author = author
        this.image = image
        this.alreadyRead = false
        Book.instances.push(this)
    }
}

let book1 = new Book("To Kill a Mockingbird","Harper Lee","https://cdn.britannica.com/21/182021-050-666DB6B1/book-cover-To-Kill-a-Mockingbird-many-1961.jpg")

let book2 = new Book("1984","George Orwell","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXWt-KK3hnoikhyPRRVhUu1qGI9kMP0xMiyw&usqp=CAU")
book2.alreadyRead = true
BookArray = Book.instances
listBook = document.getElementsByClassName("listBook")[0]

for (let object of BookArray) {
    newArticle = document.createElement("article")
    listBook.appendChild(newArticle)

    newImg = document.createElement("img")
    newImg.src = object.image
    newImg.width = 100
    newArticle.appendChild(newImg)

    newPara = document.createElement("p")
    let textNode = document.createTextNode(object.title + "\nwritten by " + object.author)
    newPara.appendChild(textNode)
    if (object.alreadyRead === true){
        newPara.style.color = "red"
    }
    newArticle.appendChild(newPara)
     
}