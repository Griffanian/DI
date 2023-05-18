document.addEventListener("DOMContentLoaded", function() {
  const container = document.getElementById("container");
  console.log(container);

  peteElement = document.querySelector('ul:first-of-type li:last-of-type ')
  peteElement.textContent = "Richard"

  sarahElement = document.querySelector('ul:last-of-type li:nth-of-type(2)')
  sarahElement.remove()

  unoderedLists = document.querySelectorAll('ul')

  for (let element of unoderedLists){
    element.classList.add("student_list")
    element.querySelector('li:first-of-type').textContent = "Miles"
  }

  firstList = document.querySelector('ul:first-of-type')
  firstList.classList.add("university")
  firstList.classList.add("attendance")

  container.style.cssText = "background-color: lightblue; padding: 10px;"
  unoderedLists[0].querySelector('li:first-of-type').remove()
  unoderedLists[0].querySelector('li').style.cssText = "border:solid red 2px;"

  document.querySelector('body').style.cssText = "font-size: 20px;"
});
