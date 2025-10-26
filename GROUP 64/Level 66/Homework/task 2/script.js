const notVal = document.getElementById("notVal");
const notBtn = document.getElementById("notBtn");
const notOut = document.getElementById("notOut");

function checkNot() {
    const result = !notVal.checked;
    notOut.textContent = `შედეგი: ${result}`
}