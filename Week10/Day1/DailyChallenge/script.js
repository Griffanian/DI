frm = document.forms[0]

frm.addEventListener('submit',function (event){
    event.preventDefault();

    labels = document.querySelectorAll("#libform input")
    itemsDict = {}
    for (let item of labels) {
        
        if (item.value === '') {
            alert("please fill all categories before submitting")
            frm.reset()
            itemsDict = {}
            break
        } else {
            itemsDict[item.id] = item.value
        }
    }
    
    var story = "Once upon a time, there was a " + itemsDict['adjective'] + " " + itemsDict['noun'] + ". ";
    story += "This " + itemsDict['noun'] + " belonged to " + itemsDict['person'] + ". ";
    story += itemsDict['person'] + " loved to " + itemsDict['verb'] + " in " + itemsDict['place'] + ". ";
    story += "It was a " + itemsDict['adjective ']+ " place."
    
    storyElement = document.getElementById("story")
    storyElement.textContent = story

    frm.reset()
})
noun,adjective,person,verb,place

