const num1 = document.getElementById("valA");
const num2 = document.getElementById("valB");
const andBtn = document.getElementById("orNumBtn");
const andOut = document.getElementById("orNumOut");

function checkOrNum() {
    result = valA.value < 5 || valB.value < 5;
    andOut.textContent = `შედეგი: ${result}`
}
