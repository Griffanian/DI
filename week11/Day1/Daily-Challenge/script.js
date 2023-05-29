
document.getElementsByTagName("form")[0].addEventListener("submit", function(event) {
  event.preventDefault();

      var formData = {};
      var formElements = this.elements;

      for (let item of formElements) {
        var fieldName = item.name;
        var fieldValue = item.value;

        if (fieldName) {
          formData[fieldName] = fieldValue;
        }
      }

      var jsonData = JSON.stringify(formData);
      console.log(jsonData); 

})