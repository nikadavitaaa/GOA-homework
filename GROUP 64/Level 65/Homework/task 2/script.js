function changeBackground() {
    const box = document.getElementById("box");
    box.style.backgroundColor = "yellow";
}

const button = document.getElementById("bgBtn");
button.onclick = changeBackground;