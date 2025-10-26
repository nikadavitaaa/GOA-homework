function calculateSum() {
    const num1 = Number(prompt("Enter the first number"));
    const num2 = Number(prompt("Enter the second number"));

    const sum = num1 + num2;

    document.getElementById("calcOut").textContent = "Sum: " + sum;
}