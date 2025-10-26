const checkBox1 = document.getElementById("input1");
const checkBox2 = document.getElementById("input2");
const button = document.getElementById("checkBtn");
const resultP = document.getElementById("result");

button.onclick = function() {
    const value1 = checkBox1.checked;
    const value2 = checkBox2.checked;

    const result = value1 && value2;

    resultP.textContent = `შედეგი: ${result}`
}