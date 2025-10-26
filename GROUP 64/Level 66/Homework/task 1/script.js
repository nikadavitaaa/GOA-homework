const value1 = document.getElementById("val1");
const value2 = document.getElementById("val2");
const orBtn = document.getElementById("orBtn");
const orOut = document.getElementById("orOut");

orBtn.onclick = function() {
    const val1 = value1.checked;
    const val2 = value2.checked;
    
    const result = val1 || val2;
    orOut.textContent = `შედეგი: ${result}`
}