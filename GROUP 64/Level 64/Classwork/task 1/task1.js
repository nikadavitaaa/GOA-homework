const user = document.getElementById("username")
const password = document.getElementById("password")
const button = document.getElementById("sub")

button.onclick = function () {
    console.log(user.value)
    console.log(password.value)

    const combined = user.value + password.value
    console.log(combined)
}
