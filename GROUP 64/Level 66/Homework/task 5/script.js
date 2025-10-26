const age = document.getElementById("age")
const ageBtn = document.getElementById("ageBtn")
const resP = document.getElementById("ageOut")

function checkAge() {
    if (age.value >= 13 && age.value <= 17) {
        resP.textContent = "Teenager"
    }
    else {
        resP.textContent = "Not teenager"
    }
}
