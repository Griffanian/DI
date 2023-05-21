var box = document.getElementById("animate");
var position = 0;
var finished = false;
var intervalId;

function myMove() {
  intervalId = setInterval(moveDiv, 10); 
}

function moveDiv() {
    if (finished === true) {
        position = 0;
        box.style.left = position + "px";
        finished = false
    }
    if (position >= 350) {
        clearInterval(intervalId);
        finished = true
    } else {
        position += 1;
        box.style.left = position + "px";
    }

}
