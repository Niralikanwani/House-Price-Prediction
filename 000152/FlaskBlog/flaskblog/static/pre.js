function validationForm() {
  var x = document.forms["MyForm"]["Bedroom"].value;
   if (x==" "||x<0) {
    alert("Please Enter correct no of bedrooms");
    return false;
  }
  var y= document.forms["MyForm"]["Bathroom"].value;
  if (y==" "||y<0) {
    alert("Please Enter correct no of Bathroom");
    return false;
  }
  var sq_liv = document.forms["MyForm"]["sqft_living"].value;
  if(sq_liv < 250){
    alert("Area of living room cannot be less then 250sqft");
    return false;
  }
  var sq_above = document.forms["MyForm"]["sqft_Above"].value;
  if(sq_above < 290){
    alert("Area of above floor cannot be less then 290sqft");
    return false;
  }
  var year = document.forms["MyForm"]["YrBuilt"].value;
  if (year.length != 4) {
            alert("Year is not proper. Please check");
            return false;
   }
   var current_year=new Date().getFullYear();
        if(year > current_year || year < 1800)
            {
            alert("Year should be less then current year");
            return false;
            }
  var elementValue =document.forms["MyForm"]["zip_code"].value;
   var zipCodePattern = /^\d{5}$|^\d{5}-\d{4}$/;
   if(zipCodePattern.test(elementValue) == false){
   alert("Enter the correct zipcode");
    return false;
  }
  alert("All input fields have been validated!");
    return true;
}