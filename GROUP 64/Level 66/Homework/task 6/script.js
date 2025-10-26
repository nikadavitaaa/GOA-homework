function checkEntry() {
    const input1 = document.getElementById("ticket").checked
    const input2 = document.getElementById("friend").checked
    const result = document.getElementById("entryOut")

    if (input1 && input2) {
        result.textContent = `შეგიძლიათ შესვლა`
    }
    else {
        result.textContent = `არ შეგიძლიათ შესვლა`
    }
}
