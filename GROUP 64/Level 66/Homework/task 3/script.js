const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const andBtn = document.getElementById("andBtn");
const andOut = document.getElementById("andOut");

function checkAnd() {
    result = num1.value > 10 && num2.value > 10;
    andOut.textContent = `შედეგი: ${result}`
}
