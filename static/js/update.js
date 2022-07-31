function checkEmail() {
    var email = document.getElementById("email");
    var filter_email = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (!filter_email.test(email.value)) {
        return false;
    }
    else
        return true;
}
let idInput = document.querySelector("#ID");  
let nameInput = document.getElementById("name");
let mobileInput = document.getElementById("mobile");
let gpaInput = document.getElementById("gpa");
let emailInput = document.getElementById("email");
let dateInput = document.getElementById("date");
let levelInput = document.getElementById("level");
document.forms[0].onsubmit = function (e) {
    if (idInput.value.length === 0 || idInput.value.length > 8) {
        e.preventDefault();
        alert("ID is not valid");
    } 
    if (nameInput.value.length === 0) {
        e.preventDefault();
        alert("Name is not valid");
    }
    if (gpaInput.value > 4 || gpaInput.value < 0 || gpaInput.value.length === 0) {
        e.preventDefault();
        alert("GPA is not valid");
    }
    if (!levelInput.value) {
        e.preventDefault();
        alert("Level is not valid");
    }
    if (!checkEmail()) {
        e.preventDefault();
        alert("Email is not valid");
    }
    if (mobile.value.length > 0 || mobile.value.length < 12 || mobile.value !== "") {
        e.preventDefault();
        alert("Mobile is not valid");
    } 
}
