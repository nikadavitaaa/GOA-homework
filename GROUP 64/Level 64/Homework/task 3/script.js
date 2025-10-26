function compareNumbers() {
    const num1 = Number(prompt("Enter the first number"));
    const num2 = Number(prompt("Enter the second number"));
    
    const output = document.getElementById("compOut");

    if (num1 > num2) {
        output.textContent = num1 + " is greater than " + num2;
    } else if (num2 > num1) {
        output.textContent = num2 + " is greater than " + num1;
    } else {
        output.textContent = "Both numbers are equal";
    }
}