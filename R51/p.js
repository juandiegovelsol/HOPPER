/*form and alert calling */

let form = document.getElementsByTagName("form")[0];
let alert = document.getElementsByClassName("alert")[0];

/*RegExp conditions for each input */
let creditCard = /^[0-9]{13,16}$/;
let isCVC = /^[0-9]{3,4}$/;
let Amount = /^[0-9]{1,}$/;
let firstName = /^[a-zA-Z]{3,}$/;
let lastName = /^[a-zA-Z]{3,}$/;
let City = /^[a-zA-Z\s]{3,}$/;
let Postal = /^[0-9]{4,9}$/;
let Message = /^[a-zA-Z,.?\s]{1,}$/; /*includes point, question mark, spaces*/

/*prevent.Default until all fields are complete */
form.addEventListener("submit", (deliver) => {
  deliver.preventDefault();
  /*getting inputs*/
  let numCrd = document.getElementById("numCard");
  let CVCCard = document.getElementById("CVCCard");
  let amountCard = document.getElementById("amountCard");
  let inName = document.getElementById("inName");
  let inCity = document.getElementById("inCity");
  let inLast = document.getElementById("inLast");
  let usState = document.getElementById("usState");
  let psCode = document.getElementById("psCode");
  let mssg = document.getElementById("mssg");
  let fullSub = true; /*all requirements are met*/

  /*check all failure points*/

  /*failure for Credit Card Number*/
  if (numCrd == "" || !creditCard.test(numCrd.value)) {
    fullSub = false;
    numCrd.classList.remove("is-valid");
    numCrd.classList.add("is-invalid");
    let selectError = document.getElementById("numCardError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    numCrd.classList.add("is-valid");
    numCrd.classList.remove("is-invalid");
  }

  /*failure for CVC number*/
  if (CVCCard == "" || !isCVC.test(CVCCard.value)) {
    fullSub = false;
    CVCCard.classList.remove("is-valid");
    CVCCard.classList.add("is-invalid");
    let selectError = document.getElementById("CVCCardError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    CVCCard.classList.add("is-valid");
    CVCCard.classList.remove("is-invalid");
  }

  /*failure for amount*/
  if (amountCard == "" || !Amount.test(amountCard.value)) {
    fullSub = false;
    amountCard.classList.remove("is-valid");
    amountCard.classList.add("is-invalid");
    let selectError = document.getElementById("amountCardError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    amountCard.classList.add("is-valid");
    amountCard.classList.remove("is-invalid");
  }

  /*failure for first name*/
  if (inName == "" || !firstName.test(inName.value)) {
    fullSub = false;
    inName.classList.remove("is-valid");
    inName.classList.add("is-invalid");
    let selectError = document.getElementById("inNameError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    inName.classList.add("is-valid");
    inName.classList.remove("is-invalid");
  }

  /*failure for city*/
  if (inCity == "" || !City.test(inCity.value)) {
    fullSub = false;
    inCity.classList.remove("is-valid");
    inCity.classList.add("is-invalid");
    let selectError = document.getElementById("inCityError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    inCity.classList.add("is-valid");
    inCity.classList.remove("is-invalid");
  }

  /*failure for last name*/
  if (inLast == "" || !lastName.test(inLast.value)) {
    fullSub = false;
    inLast.classList.remove("is-valid");
    inLast.classList.add("is-invalid");
    let selectError = document.getElementById("inLastError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    inLast.classList.add("is-valid");
    inLast.classList.remove("is-invalid");
  }

  /*failure for state*/
  if (usState.value == "Pick a state") {
    fullSub = false;
    usState.classList.remove("is-valid");
    usState.classList.add("is-invalid");
    let selectError = document.getElementById("usStateError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    usState.classList.add("is-valid");
    usState.classList.remove("is-invalid");
  }

  /*failure for postal code*/
  if (psCode == "" || !Postal.test(psCode.value)) {
    fullSub = false;
    psCode.classList.remove("is-valid");
    psCode.classList.add("is-invalid");
    let selectError = document.getElementById("psCodeError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    psCode.classList.add("is-valid");
    psCode.classList.remove("is-invalid");
  }

  /*failure for message*/
  if (mssg == "" || !Message.test(mssg.value)) {
    fullSub = false;
    mssg.classList.remove("is-valid");
    mssg.classList.add("is-invalid");
    let selectError = document.getElementById("mssgError");
    selectError.classList.remove("d-none");
    alert.classList.remove("d-none");
  } else {
    /*return to normal settings*/
    mssg.classList.add("is-valid");
    mssg.classList.remove("is-invalid");
  }

  if (fullSub) {
    form.submit();
  }
});
