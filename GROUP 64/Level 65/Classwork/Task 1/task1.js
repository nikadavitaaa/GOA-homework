function resultgetorsomething() {
    let check1 = document.getElementById("checkbx1");
    let check2 = document.getElementById("checkbx2");
    let resultOut = document.getElementById("resultOut");

    let val1 = check1.checked;
    let val2 = check2.checked;
    let result = val1 && val2;

    resultOut.textContent = "Result: " + result;
}
